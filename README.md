# racing_web_api
Using the Python api from https://github.com/jeysonmc/ir_webstats
to publish the racing schedule and racing session statistics.
Some examples:

+-------------------------------------+----------------------------------------------+---------------------+---------------+
|             Racing serie            |                    Track                     |     Next session    | Num registred |
+-------------------------------------+----------------------------------------------+---------------------+---------------+
|    Advanced Mazda MX-5 Cup Series   |        Sebring International Raceway         | 2018-11-02 21:15:00 |       0       |
|       Classic Lotus Grand Prix      |       Detroit Grand Prix at Belle Isle       | 2018-11-02 19:30:00 |       0       |
|       Fanatec Global Challenge      | Autodromo Internazionale Enzo e Dino Ferrari | 2018-11-02 20:30:00 |       0       |
|         Fanatec GT Challenge        |         Circuit de Spa-Francorchamps         | 2018-11-02 20:45:00 |       0       |
|    Ferrari GT3 Challenge - Fixed    |      WeatherTech Raceway at Laguna Seca      | 2018-11-02 19:30:00 |       26      |
|        Global Mazda MX-5 Cup        |        Okayama International Circuit         | 2018-11-02 20:00:00 |       0       |
|          Grand Prix Legends         | Autodromo Internazionale Enzo e Dino Ferrari | 2018-11-02 20:30:00 |       0       |
|     IMSA Sportscar Championship     |          Autódromo José Carlos Pace          | 2018-11-02 19:45:00 |       4       |
|         Industriefahrten Fun        |           Nürburgring Nordschleife           | 2018-11-02 19:30:00 |       2       |
|        IndyCar Series - Road        |                 ISM Raceway                  | 2018-11-02 21:00:00 |       0       |
|   iRacing Endurance Le Mans Series  |          Autodromo Nazionale Monza           | 2018-11-03 08:00:00 |       0       |
|     iRacing Formula Renault 2.0     |          Watkins Glen International          | 2018-11-02 19:45:00 |       0       |
|     iRacing Grand Touring Cup MC    |            Mount Panorama Circuit            | 2018-11-02 20:15:00 |       0       |
|        iRacing Le Mans Series       |          Autodromo Nazionale Monza           | 2018-11-02 20:00:00 |       0       |
| iRacing Production Car Challenge MC |            Pocono Raceway - 2011             | 2018-11-02 19:30:00 |       7       |
|  iRacing Spec Racer Ford Challenge  |          Circuit Gilles Villeneuve           | 2018-11-02 19:45:00 |       1       |
|     iRacing V8 Supercars Series     |             Brands Hatch Circuit             | 2018-11-02 21:15:00 |       0       |
|        Kamel GT Championship        |        Sebring International Raceway         | 2018-11-02 20:00:00 |       0       |
|         Porsche iRacing Cup         |            Mount Panorama Circuit            | 2018-11-02 20:45:00 |       0       |
|        Pro Mazda Championship       |          Watkins Glen International          | 2018-11-02 20:45:00 |       0       |
|      Radical Racing Challenge C     |          Watkins Glen International          | 2018-11-02 20:00:00 |       0       |
|          Ruf GT3 Challenge          |                 Road America                 | 2018-11-02 20:00:00 |       0       |
|       Skip Barber Race Series       |       Detroit Grand Prix at Belle Isle       | 2018-11-02 20:15:00 |       0       |
|       VRS GT Endurance Series       |          Autodromo Nazionale Monza           | 2018-11-03 10:00:00 |       0       |
|         VRS GT Sprint Series        |          Autodromo Nazionale Monza           | 2018-11-02 21:00:00 |       0       |
+-------------------------------------+----------------------------------------------+---------------------+---------------+
+---------------------------------------------+-----------------------------+---------------------+---------------+
|                 Racing serie                |            Track            |     Next session    | Num registred |
+---------------------------------------------+-----------------------------+---------------------+---------------+
|            AMSOIL USAC Sprint Car           | The Dirt Track at Charlotte | 2018-11-02 20:45:00 |       0       |
|        DIRTcar 305 Sprint Car Series        |      Knoxville Raceway      | 2018-11-02 20:00:00 |       0       |
|        DIRTcar 360 Sprint Car Series        |    Volusia Speedway Park    | 2018-11-02 20:30:00 |       0       |
| DIRTcar Class C Street Stock Series - Fixed |    Volusia Speedway Park    | 2018-11-02 21:00:00 |       0       |
|      DIRTcar Limited Late Model Series      |       Kokomo Speedway       | 2018-11-02 20:00:00 |       0       |
|        DIRTcar Pro Late Model Series        |   Williams Grove Speedway   | 2018-11-02 19:30:00 |       6       |
|         DIRTcar UMP Modified Series         |    Volusia Speedway Park    | 2018-11-02 20:15:00 |       0       |
|           iRacing Dirt Legends Cup          |  Limaland Motorsports Park  | 2018-11-02 19:45:00 |       0       |
|           iRacing Dirt Midget Cup           |       Kokomo Speedway       | 2018-11-02 20:15:00 |       0       |
|       Sling Mud for Fun - Late Models       | The Dirt Track at Charlotte | 2018-11-02 19:30:00 |       5       |
|       Sling Mud for Fun - Sprint Cars       |    Volusia Speedway Park    | 2018-11-02 20:00:00 |       0       |
|          USAC 360 Sprint Car Series         |       Eldora Speedway       | 2018-11-02 19:45:00 |       0       |
|     World of Outlaws Late Model Series      | The Dirt Track at Charlotte | 2018-11-02 20:45:00 |       0       |
|      World of Outlaws Sprint Car Series     |      Knoxville Raceway      | 2018-11-02 19:30:00 |       0       |
+---------------------------------------------+-----------------------------+---------------------+---------------+
+----------------------------------+---------------------------------------+---------------------+---------------+
|           Racing serie           |                 Track                 |     Next session    | Num registred |
+----------------------------------+---------------------------------------+---------------------+---------------+
|    iRacing Rallycross Series     |           Lucas Oil Raceway           | 2018-11-02 20:00:00 |       0       |
| Rookie iRacing Rallycross Series | Daytona International Speedway - 2007 | 2018-11-02 19:30:00 |       9       |
+----------------------------------+---------------------------------------+---------------------+---------------+

Ruf GT3 Challenge
+----------+--------+----------+----------+----------+--------+----------+--------+
|   Time   | Monday | Thuesday | Wendsday | Thursday | Friday | Saturday | Sunday |
+----------+--------+----------+----------+----------+--------+----------+--------+
| 00:00:00 |   0    |    0     |    1     |    0     |   0    |    0     |   0    |
| 01:00:00 |   5    |    3     |    7     |    8     |   7    |    4     |   7    |
| 02:00:00 |   0    |    0     |    0     |    0     |   0    |    0     |   0    |
| 03:00:00 |   5    |    2     |    4     |    4     |   3    |    5     |   3    |
| 04:00:00 |   0    |    0     |    0     |    0     |   0    |    0     |   1    |
| 05:00:00 |   2    |    2     |    2     |    1     |   1    |    5     |   2    |
| 06:00:00 |   0    |    0     |    0     |    0     |   0    |    0     |   0    |
| 07:00:00 |   0    |    1     |    1     |    0     |   1    |    1     |   3    |
| 08:00:00 |   0    |    0     |    0     |    0     |   0    |    0     |   0    |
| 09:00:00 |   1    |    1     |    2     |    2     |   1    |    3     |   1    |
| 10:00:00 |   1    |    0     |    0     |    0     |   0    |    0     |   2    |
| 11:00:00 |   1    |    1     |    2     |    2     |   1    |    6     |   13   |
| 12:00:00 |   1    |    0     |    0     |    0     |   0    |    0     |   1    |
| 13:00:00 |   2    |    5     |    1     |    5     |   2    |    9     |   11   |
| 14:00:00 |   0    |    0     |    0     |    0     |   1    |    0     |   0    |
| 15:00:00 |   5    |    2     |    4     |    1     |   3    |    10    |   10   |
| 16:00:00 |   0    |    0     |    1     |    0     |   0    |    0     |   1    |
| 17:00:00 |   7    |    4     |    9     |    3     |   9    |    16    |   17   |
| 18:00:00 |   0    |    0     |    1     |    1     |   0    |    0     |   2    |
| 19:00:00 |   12   |    11    |    12    |    9     |   11   |    15    |   19   |
| 20:00:00 |   0    |    1     |    1     |    1     |   0    |    0     |   0    |
| 21:00:00 |   14   |    12    |    12    |    17    |   15   |    13    |   16   |
| 22:00:00 |   0    |    2     |    0     |    0     |   0    |    0     |   1    |
| 23:00:00 |   14   |    11    |    12    |    13    |   11   |    11    |   14   |
+----------+--------+----------+----------+----------+--------+----------+--------+
Skip Barber Race Series
+----------+--------+----------+----------+----------+--------+----------+--------+
|   Time   | Monday | Thuesday | Wendsday | Thursday | Friday | Saturday | Sunday |
+----------+--------+----------+----------+----------+--------+----------+--------+
| 00:15:00 |   42   |    42    |    50    |    53    |   43   |    53    |   49   |
| 01:15:00 |   39   |    37    |    42    |    41    |   37   |    42    |   41   |
| 02:15:00 |   34   |    38    |    41    |    39    |   31   |    33    |   36   |
| 03:15:00 |   32   |    33    |    39    |    35    |   34   |    29    |   33   |
| 04:15:00 |   27   |    29    |    33    |    30    |   30   |    35    |   28   |
| 05:15:00 |   22   |    25    |    26    |    26    |   26   |    30    |   32   |
| 06:15:00 |   18   |    21    |    21    |    23    |   21   |    23    |   24   |
| 07:15:00 |   16   |    17    |    14    |    16    |   16   |    21    |   18   |
| 08:15:00 |   11   |    12    |    11    |    14    |   14   |    16    |   18   |
| 09:15:00 |   12   |    14    |    13    |    16    |   13   |    17    |   17   |
| 10:15:00 |   15   |    21    |    21    |    20    |   20   |    21    |   24   |
| 11:15:00 |   26   |    23    |    28    |    26    |   23   |    28    |   32   |
| 12:15:00 |   34   |    25    |    29    |    30    |   25   |    31    |   37   |
| 13:15:00 |   30   |    28    |    29    |    30    |   25   |    32    |   39   |
| 14:15:00 |   18   |    25    |    27    |    25    |   27   |    29    |   34   |
| 15:15:00 |   22   |    20    |    26    |    19    |   31   |    39    |   41   |
| 16:15:00 |   23   |    22    |    31    |    25    |   34   |    44    |   49   |
| 17:15:00 |   32   |    30    |    33    |    27    |   38   |    43    |   55   |
| 18:15:00 |   35   |    41    |    41    |    32    |   48   |    43    |   57   |
| 19:15:00 |   41   |    51    |    48    |    44    |   46   |    52    |   58   |
| 20:15:00 |   49   |    50    |    50    |    51    |   47   |    53    |   61   |
| 21:15:00 |   46   |    55    |    53    |    62    |   51   |    53    |   56   |
| 22:15:00 |   47   |    59    |    53    |    54    |   57   |    59    |   47   |
| 23:15:00 |   48   |    58    |    59    |    53    |   60   |    55    |   57   |
+----------+--------+----------+----------+----------+--------+----------+--------+
VRS GT Endurance Series
+----------+--------+----------+----------+----------+--------+----------+--------+
|   Time   | Monday | Thuesday | Wendsday | Thursday | Friday | Saturday | Sunday |
+----------+--------+----------+----------+----------+--------+----------+--------+
| 11:00:00 |   0    |    0     |    0     |    0     |   0    |    27    |   0    |
| 18:00:00 |   0    |    0     |    0     |    0     |   0    |    0     |   9    |
| 19:00:00 |   0    |    0     |    0     |    0     |   0    |    0     |   59   |
| 21:00:00 |   0    |    0     |    0     |    0     |   0    |    62    |   0    |
+----------+--------+----------+----------+----------+--------+----------+--------+
