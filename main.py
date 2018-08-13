import argparse as ap
import time
import datetime

from ir_webstats.client import iRWebStats
from ir_webstats.util import *

from prettytable import PrettyTable


if __name__ == '__main__':

    parser = ap.ArgumentParser(description="Shell interface for iRWebStats")
    parser.add_argument("-u", "--user", help='iRacing user', required=False)
    parser.add_argument("-p", "--passw", help='iRacing password',required=False)

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

    season_stat = irw.all_seasons()

    road_serie = [serie for serie in season_stat if
                  serie['licenseEligible'] is True and serie['category'] == 2]
    dirt_road_serie = [serie for serie in season_stat if
                       serie['licenseEligible'] is True and serie['category'] == 4]
    dirt_oval_serie = [serie for serie in season_stat
                       if serie['licenseEligible'] is True and serie['category'] == 3]

    def print_serie(series):
        x = PrettyTable()
        x.field_names = ["Racing serie", "Track", "Next session"]

        for serie in series:
            name = serie['seriesname']
            #print(name)
            times = irw.session_times(serie['seasonid'], 0, 1000000)
            next_sessions = times['d']

            if len(next_sessions) == 0:
                continue

            # Get the racing sessions.
            next_racing_sessions = [session for session in next_sessions['r'] if session['9'] == 5]

            next_session_time = next_racing_sessions[0]['6']

            next_sessiont_time_string = \
                datetime.datetime.fromtimestamp(next_session_time / 1e3).strftime('%Y-%m-%d %H:%M:%S')

            current_week = serie['raceweek']
            tracks = serie['tracks']
            current_track = tracks[current_week-1]['name']

            x.add_row([name, current_track, next_sessiont_time_string])

        print(x)

    print_serie(road_serie)
    print_serie(dirt_oval_serie)
    print_serie(dirt_road_serie)
