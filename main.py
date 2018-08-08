import argparse as ap

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

    season_stat = irw.all_seasons()

    road_serie = [serie for serie in season_stat if
                  serie['licenseEligible'] is True and serie['category'] == 2]
    dirt_road_serie = [serie for serie in season_stat if
                       serie['licenseEligible'] is True and serie['category'] == 4]
    dirt_oval_serie = [serie for serie in season_stat
                       if serie['licenseEligible'] is True and serie['category'] == 3]


    def print_serie(series):
        x = PrettyTable()
        x.field_names = ["Racing serie", "Track"]

        for serie in series:
            name = serie['seriesname']
            current_week = serie['raceweek']
            tracks = serie['tracks']
            if len(tracks) == 1:
                current_week = 0
            current_track = tracks[current_week]['name']

            x.add_row([name, current_track])

        print(x)


    print_serie(dirt_oval_serie)
    print_serie(dirt_road_serie)
    print_serie(road_serie)