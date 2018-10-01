import argparse as ap
import time
import datetime
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
        summed_field_size = []
        all_times = [d['time'] for d in weekly_data]
        times = list(set(all_times))
        times.sort()
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
                else:
                    field_size_per_time['weekday'] = i
                    field_size_per_time['time'] = time
                    field_size_per_time['total_field'] = 0
                    summed_field_size_per_day.append(field_size_per_time)
            summed_field_size.append(summed_field_size_per_day)

        y = PrettyTable()
        column_names = ["Time", "Monday", "Thuesday", "Wendsday", "Thursday",
                        "Friday", "Saturday", "Sunday"]
        y.add_column(column_names[0], times)
        for races_per_day in summed_field_size: #For each day
            if len(races_per_day) == 0:
                continue
            total_field_per_day = [d['total_field'] for d in races_per_day]
            time_per_day = [d['time'].strftime('%H:%M') for d in races_per_day]
            weekdays = [d['weekday'] for d in races_per_day]
            y.add_column(column_names[weekdays[0]+1], total_field_per_day)
            if len(time_per_day) == 0:
                time2 = time_per_day
                summed_field = total_field_per_day
                weekday = weekdays
            else:
                for i in range(len(total_field_per_day)):
                    time2 = time_per_day[i]
                    summed_field = total_field_per_day[i]
                    weekday = weekdays[i]

        print(y)
        print("Finnished")





