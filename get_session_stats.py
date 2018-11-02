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

    print("Current time is: ")
    current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print(current_time)
    season = ''
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
                    data['raceweek'] = race_week

                    weekly_data.append(dp(data))
            serie_data['weekly_data'] = weekly_data
            total.append(serie_data)
        return total

    season_stat = irw.all_seasons()

    season = season_stat[5]['seasonshortname']
    print('season: {}'.format(season))
    current_race_week = season_stat[5]['raceweek']
    # get racing series data for road racing.
    # 1=oval, 2=road, 3=dirt_oval, 4=dirt_road
    road_series_stat = [serie for serie in season_stat if
                        serie['licenseEligible'] is True and serie['category'] == 2]
    series_data = get_data(road_series_stat)

    current_time_ts = time.time()
    print("Current time is: ")
    st = datetime.datetime.fromtimestamp(current_time_ts).strftime('%Y-%m-%d %H:%M:%S')
    print(st)

    print('all data recieved. Start processing')
    filename = 'racing_stat' + '.html'
    with open(filename, 'w') as f:
        f.write('Generated data at {current_time} for season {season}, '
                'raceweek {raceweek} <br> '.format(
                 current_time=current_time, season=season, raceweek=current_race_week))
        for serie_data in series_data:
            weekly_data = serie_data['weekly_data']
            print(serie_data['serie_name'])
            f.write('\n Race session data for {serie_name} <br>'.format(
                serie_name=serie_data['serie_name']))
            # get all time. Using Wendsday as reference
            summed_field_size = []
            all_times = [d['time'] for d in weekly_data]
            times = list(set(all_times))
            all_raceweeks = [d['raceweek'] for d in weekly_data]
            unique_raceweeks = list(set(all_raceweeks))
            times.sort()
            for i in range(0,7):
                summed_field_size_per_day = []
                for time in times:
                    sum_field_size = 0
                    for raceweek in unique_raceweeks:
                        field_size_per_time = {}
                        session_at_time_and_day = [d for d in weekly_data if d['weekday'] == i and
                                                   d['time'] == time and d['raceweek'] == raceweek]
                        if len(session_at_time_and_day) > 0:
                            field_sizes = [oo['field_size'] for oo in session_at_time_and_day]
                            #num_field = len(field_sizes)
                            sum_field = sum(field_sizes)
                            field_size = sum_field
                        else:
                            field_size = 0
                        sum_field_size += field_size

                    field_size_per_time['weekday'] = i
                    field_size_per_time['time'] = time
                    field_size_per_time['total_field'] = \
                        int(round(sum_field_size) / len(unique_raceweeks))
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
            f.write(y.get_html_string())
            f.write('\n')
    print("Complete")







