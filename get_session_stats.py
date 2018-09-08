import argparse as ap
import time
import datetime

import matplotlib.pyplot as plt
from ir_webstats.client import iRWebStats
from ir_webstats.util import *

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


    def get_data(road_serie):
        total = []
        for serie in road_serie:
            #if len(serie['tracks']) == 0:
            #    continue
            serie_data = {}
            serie_data['serie_name'] = serie['seriesname']
            weekly_data = []
            all_data = []
            for i in serie['tracks']:
                race_week = i['raceweek']
                series_results = irw.series_raceresults(int(serie['seasonid']), race_week)
                #current_week = serie['raceweek']
                #num_weeks = serie['tracks']

                accum = []
                previous_start_time = 0
                for j in series_results:

                    data = {}
                    start_time = j['start_time']
                    field_size = j['sizeoffield']
                    #if j == 0:
                    #    previous_start_time = start_time
                    #elif start_time == previous_start_time:
                    #    accum[j-1]['field_size'] += field_size
                    #    previous_start_time = start_time
                    #    continue

                    data['start_time'] = start_time
                    data['field_size'] = field_size

                    next_sessiont_time_string = \
                        datetime.datetime.fromtimestamp(start_time / 1e3).strftime('%Y-%m-%d %H:%M:%S')
                    data['start_time_str'] = next_sessiont_time_string
                    accum.append(data)
                    all_data.append(data)
                for start_time, size, _  in data:

                weekly_data.append(accum)
            serie_data['weekly_data'] = all_data
            total.append(serie_data)
        return total

    season_stat = irw.all_seasons()

    road_serie2 = [serie for serie in season_stat if
                  serie['licenseEligible'] is True and serie['category'] == 2]
    data = get_data(road_serie2)
    sizey = [xx['field_size'] for xx in data[0]['weekly_data']]
    times = [xx['start_time'] for xx in data[0]['weekly_data']]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.stackplot(times, sizey)
    ax.set_title('Sessions')
    ax.legend(loc='upper left')
    ax.set_ylabel('Field size')
    #ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])

    print("Finnished")





