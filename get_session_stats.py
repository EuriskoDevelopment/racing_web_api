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

    def get_data(road_serie):
        # Get data from URL adress to iracing
        total = []
        for serie in road_serie:
            print('getting data for:')
            print(serie['seriesname'])
            serie_data = {}
            serie_data['serie_name'] = serie['seriesname']
            weekly_data = []

            for i in serie['tracks']:
                race_week = i['raceweek']
                series_results = irw.series_raceresults(int(serie['seasonid']), race_week)

                for j in series_results:
                    data = {}
                    start_time = j['start_time']
                    field_size = j['sizeoffield']

                    start_time_obj = datetime.datetime.fromtimestamp(start_time / 1e3)
                    session_weekday = start_time_obj.weekday()
                    session_time = start_time_obj.time()

                    data['weekday'] = session_weekday # 0=Monday, 1=Thuesday etc.
                    data['time'] = session_time
                    data['field_size'] = field_size

                    weekly_data.append(dp(data))
            serie_data['weekly_data'] = weekly_data
            total.append(serie_data)
        return total

    season_stat = irw.all_seasons()

    # get racing serie. 1=oval, 2=road, 3=dirt_oval, 4=dirt_road
    road_serie = [serie for serie in season_stat if
                  serie['licenseEligible'] is True and serie['category'] == 2]
    series_data = get_data(road_serie)

    print('all data recieved. Start processing')

    for serie_data in series_data:
        weekly_data = serie_data['weekly_data']
        print(serie_data['serie_name'])

        # get all time. Using Wendsday as reference
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
                    field_size_per_time['total_field'] = sum_field
                    summed_field_size_per_day.append(field_size_per_time)
            summed_field_size.append(summed_field_size_per_day)

        for races_per_day in summed_field_size:
            x = PrettyTable()
            x.field_names = ["Weekday", "Time", "Field size"]
            if len(races_per_day) == 0:
                continue
            races_per_day.sort(key=lambda item: item['time'], reverse=True)

            avgs_wends = [d['total_field'] for d in races_per_day]
            times_wends = [d['time'] for d in races_per_day]
            weekdays = [d['weekday'] for d in races_per_day]
            if len(avgs_wends) == 1:
                print(len(avgs_wends))
                print(" ++++++++ ++++++++++ +++++++++ ")
                continue
            else:
                for i in range(len(avgs_wends)):
                    time2 = times_wends[i].strftime('%H:%M')
                    summed_field = avgs_wends[i]
                    weekday = weekdays[i]
                    x.add_row([weekday, time2, summed_field])
            print(x)

        print("Finnished")





