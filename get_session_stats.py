import argparse as ap
import time
import datetime
import matplotlib.pyplot as plt
from ir_webstats.client import iRWebStats
from copy import deepcopy as dp
from prettytable import PrettyTable

if __name__ == '__main__':

    parser = ap.ArgumentParser(description="Shell interface for iRWebStats")
    parser.add_argument("-u", "--user", help='iRacing user', required=False)
    parser.add_argument("-p", "--passw", help='iRacing password', required=False)

    args = parser.parse_args()

    irw = iRWebStats()

    if args.user and args.passw:
        irw.login(username=args.user, password=args.passw)
    else:
        print("Check if valid cookie and then try to log in")
        irw.login()  # No login provided, maybe there's a valid cookie

    if not irw.logged:
        print(
            "Couldn't log in to iRacing Membersite. Please check your credentials")
        exit()

    print("Succes login")

    current_time_ts = time.time()
    print("Current time is: ")
    st = datetime.datetime.fromtimestamp(current_time_ts).strftime('%Y-%m-%d %H:%M:%S')
    print(st)

    #results = irw.results_archive(irw.custid)
    x = PrettyTable()
    x.field_names = ["Time", "Field size"]

    def get_data(road_serie):
        total = []
        for serie in road_serie:
            #if len(serie['tracks']) == 0:
            #    continue
            print('getting data for:')
            print(serie['seriesname'])
            serie_data = {}
            serie_data['serie_name'] = serie['seriesname']
            weekly_data = []
            all_data = []

            for i in serie['tracks']:

                race_week = i['raceweek']
                series_results = irw.series_raceresults(int(serie['seasonid']), race_week)
                #current_week = serie['raceweek']
                #num_weeks = serie['tracks']

                weekday_ = []
                previous_start_time = 0

                for j in series_results:
                    data = {}
                    #data = {}
                    start_time = j['start_time']
                    field_size = j['sizeoffield']
                    #if j == 0:
                    #    previous_start_time = start_time
                    #elif start_time == previous_start_time:
                    #    accum[j-1]['field_size'] += field_size
                    #    previous_start_time = start_time
                    #    continue

                    #data[start_time] += field_size
                    #data['field_size'] = field_size

                    start_time_obj = datetime.datetime.fromtimestamp(start_time / 1e3)
                    weekday = start_time_obj.weekday()
                    start_time_str = \
                        datetime.datetime.fromtimestamp(start_time / 1e3).strftime('%Y-%m-%d %H:%M:%S')
                    #data['start_time_str'] = next_sessiont_time_string
                    datetime_week = datetime.timedelta(weeks=1)

                    #print(weekday)
                    time = start_time_obj.time()
                    #print(time)

                    data['weekday'] = weekday
                    data['time'] = time
                    data['field_size'] = field_size
                    #data['num']
                    #for kk in data:
                        #if start_time_str == kk - datetime_week

                    weekly_data.append(dp(data))
                    #if
                    #data3 = weekday_list[weekday]

                    #if time in data3:
                    #    data['time'] = time
                    #    data['num'] += 1
                    #else:
                    #    data[time] = field_size
                    #    data['num'] = 0

                        #accum.append(data)
                    #all_data.append(data)
#                for start_time, size, _  in data:

                #weekly_data.append(accum)
            serie_data['weekly_data'] = weekly_data
            total.append(serie_data)
        return total

    season_stat = irw.all_seasons()

    road_serie = [serie for serie in season_stat if
                  serie['licenseEligible'] is True and serie['category'] == 2] #2 is actual road
    series_data = get_data(road_serie)
    print('all data recieved. Start processing')

    # for serie_data in series_data:
    serie_data = series_data[7]
    weekly_data = serie_data['weekly_data']
    print(serie_data['serie_name'])

    # get all time. Using Wendsday as referance
    times2 = [d['time'] for d in weekly_data if d['weekday'] == 2]

    times = set(times2)
    summed_field_size = []
    for i in range(0,7):
        summed_field_size_per_day = []
        for time in times:
            field_size_per_time = {}
            dd = [d for d in weekly_data if d['weekday'] == i and d['time'] == time]
            if len(dd) > 0:
                kk = [oo['field_size'] for oo in dd]
                num_field = len(kk)
                sum_field = sum(kk)
                field_size_per_time['weekday'] = i
                field_size_per_time['time'] = time
                field_size_per_time['avg_field'] = sum_field
                summed_field_size_per_day.append(field_size_per_time)
        summed_field_size.append(summed_field_size_per_day)

    #for daily_data in summed_field_size:
    #    #daily_data = summed_field_size[i]

    for races_per_day in summed_field_size:
        if len(races_per_day) == 0:
            continue
        races_per_day.sort(key=lambda item: item['time'], reverse=True)

        avgs_wends = [d['avg_field'] for d in races_per_day]
        times_wends = [d['time'] for d in races_per_day]
        if len(avgs_wends) == 1:
            #x.add_column(times_wends, avgs_wends)
            continue
        else:
            for i in range(len(avgs_wends)):
                time2 = times_wends[i].strftime('%H:%M')
                summed_field = avgs_wends[i]
                x.add_row([time2, summed_field])
    #plt.bar(range(len(times_wends)), avgs_wends, align='center')
    #plt.xticks(range(len(avgs_wends)), times_wends)
    #plt.show()
    print(x)
    print("Finnished")





