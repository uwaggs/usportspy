# USPORTSPY - One-Stop-Shop for USPORTS Data
<!-- ![](usportspy.png =200x) -->



## Disclaimer
This package is still early in development, and is subject to unexpected changes. If you'd still like to try this out, be sure to only use the latest package.


Documentation can be found in the [wiki](https://github.com/uwaggs/usportspy/wiki)

## Included Sports
- [X] Wrestling
- [X] Volleyball
- [X] Ice Hockey
- [X] Swimming
- [X] Track & Field
- [X] Cross Country
- [X] Basketball
- [X] Field Hockey
- [X] Soccer
- [X] Rugby
- [X] Football

<!-- 
## Wrestling Documentation

#### `wrestling_athlete_rankings(gender, weight)`
- `gender`: can be either `"MALE"` or `"FEMALE"`
- `weight`: an integer representing the weight class to return data for in kilograms.
- Returns a pandas dataframe with the columns `Weight Category`, `Rank`, `School`, `Last Updated`. 

#### `wrestling_team_rankings(gender)`
- `gender`: can be either `"MALE"` or `"FEMALE"`
- Returns a pandas dataframe with the columns `Rank`, `School`, `Points`, `Previous Rank`, `Last Updated`. 
 

Example usage:
```Python
from usportspy import wrestling_athlete_rankings, wrestling_team_rankings
print(wrestling_team_rankings("MALE"))
print(wrestling_team_rankings("FEMALE"))
print(wrestling_athlete_rankings("MALE", 57))
print(wrestling_athlete_rankings("FEMALE", 56))
```

Expected output:
```
    Rank        School  Points Previous Rank Last Updated
0      1         Brock      81             1   02/01/2020
1      2  Saskatchewan      50             3   02/01/2020
2      3       Alberta      49             2   02/01/2020
3      4     Concordia      47             7   02/01/2020
4      5        Guelph      42             6   02/01/2020
..   ...           ...     ...           ...          ...
85     6        Guelph      29             6   01/30/2024
86     7       Western      29             7   01/30/2024
87     8        Algoma      18             8   01/30/2024
88     9      Lakehead      12            10   01/30/2024
89    10     Concordia      11             9   01/30/2024

[90 rows x 5 columns]
    Rank        School  Points Previous Rank Last Updated
0      1         Brock      50             1   02/01/2020
1      2       Calgary      45             3   02/01/2020
2      3  Saskatchewan      41             2   02/01/2020
3      4     Concordia      32             5   02/01/2020
4      5       Alberta      31             4   02/01/2020
..   ...           ...     ...           ...          ...
85     6       Western      27             7   01/30/2024
86     7     Concordia      26             8   01/30/2024
87     8      McMaster      25             6   01/30/2024
88     9      Carleton      16             8   01/30/2024
89    10          York      10             –   01/30/2024

[90 rows x 5 columns]
   Weight Category Rank                   Name        School Last Updated
0             57kg    1          Kyle Robinson        Guelph   02/01/2020
1             57kg    2       Garette Saunders         Brock   02/01/2020
2             57kg    3          Harris Valdes       Alberta   02/01/2020
3             57kg    4         Drake Buechler  Saskatchewan   02/01/2020
4             57kg    5      Francesco Fortino      McMaster   02/01/2020
..             ...  ...                    ...           ...          ...
60            57kg    4             Lucas Reid  Saskatchewan   01/30/2024
61            57kg    5        Gabe Sementilli         Brock   01/30/2024
62            57kg    6          Fred Calingay       Calgary   01/30/2024
63            57kg    7        Sullivan Valdez        Algoma   01/30/2024
64            57kg    8  Edward Matida-Torrico      Carleton   01/30/2024

[65 rows x 5 columns]
   Weight Category  Rank               Name        School Last Updated
0             56kg     1    Alexandria Town          York   11/16/2021
1             56kg     2      SueAnne Harms  Saskatchewan   11/16/2021
2             56kg     3        Vivica Addo       Alberta   11/16/2021
3             56kg     4     Grace Chambers       Calgary   11/16/2021
4             56kg     5      Macy Malysiak      McMaster   11/16/2021
5             56kg     6    Daina Armstrong         Brock   11/16/2021
6             56kg     1      SueAnne Harms  Saskatchewan   11/22/2021
7             56kg     2    Alexandria Town          York   11/22/2021
8             56kg     3      Macy Malysiak      McMaster   11/22/2021
9             56kg     4        Vivica Addo       Alberta   11/22/2021
10            56kg     5     Grace Chambers       Calgary   11/22/2021
11            56kg     6     Emalea Drozdow       Western   11/22/2021
12            56kg     1      Macy Malysiak      McMaster   10/31/2022
13            56kg     2  Robbie Ann Pingal       Alberta   10/31/2022
14            56kg     3     Gabriela Cross       Calgary   10/31/2022
15            56kg     4      Jayden Sparks        Guelph   10/31/2022
16            56kg     5      Allison Kuzub  Saskatchewan   10/31/2022
17            56kg     1  Robbie Ann Pingal       Alberta   01/30/2023
18            56kg     2    Virginie Gascon     Concordia   01/30/2023
19            56kg     3      Macy Malysiak      McMaster   01/30/2023
20            56kg     4      Jayden Sparks        Guelph   01/30/2023
21            56kg     5       Alison Kuzub  Saskatchewan   01/30/2023
22            56kg     6     Emalea Drozdow       Western   01/30/2023
23            56kg     7        Ella Jakobi         Brock   01/30/2023
24            56kg     8     Gabriela Cross       Calgary   01/30/2023
25            56kg     1        Mia Friesen         Brock   02/14/2023
26            56kg     2    Virginie Gascon     Concordia   02/14/2023
27            56kg     3     Gabriela Cross       Calgary   02/14/2023
28            56kg     4  Robbie Ann Pingal       Alberta   02/14/2023
29            56kg     5       Alison Kuzub  Saskatchewan   02/14/2023
30            56kg     6      Macy Malysiak      McMaster   02/14/2023
31            56kg     7      Jayden Sparks        Guelph   02/14/2023
32            56kg     8       Kirti Saxena       Toronto   02/14/2023
33            56kg     1      SueAnne Harms  Saskatchewan   12/05/2023
34            56kg     2        Anika Fines       Calgary   12/05/2023
35            56kg     3    Virginie Gascon     Concordia   12/05/2023
36            56kg     4     Brooklyn Brown         Brock   12/05/2023
37            56kg     5  Robbie Ann Pingal       Alberta   12/05/2023
38            56kg     6   Kendall Dettloff       Western   12/05/2023
39            56kg     7      Jayden Sparks        Guelph   12/05/2023
40            56kg     8        Mayumi King      McMaster   12/05/2023
41            56kg     1      SueAnne Harms  Saskatchewan   01/16/2024
42            56kg     2       Annika Fines       Calgary   01/16/2024
43            56kg     3     Sophia Bechard     Concordia   01/16/2024
44            56kg     4   Kendall Dettloff       Western   01/16/2024
45            56kg     5  Robbie Ann Pingal       Alberta   01/16/2024
46            56kg     6     Brooklyn Brown         Brock   01/16/2024
47            56kg     7      Jayden Sparks        Guelph   01/16/2024
48            56kg     8        Mayumi King      McMaster   01/16/2024
49            56kg     1      SueAnne Harms  Saskatchewan   01/30/2024
50            56kg     2       Annika Fines       Calgary   01/30/2024
51            56kg     3     Sophia Bechard     Concordia   01/30/2024
52            56kg     4   Kendall Dettloff       Western   01/30/2024
53            56kg     5  Robbie Ann Pingal       Alberta   01/30/2024
54            56kg     6     Brooklyn Brown         Brock   01/30/2024
55            56kg     7      Jayden Sparks        Guelph   01/30/2024
56            56kg     8        Mayumi King      McMaster   01/30/2024
```


## Swimming Documentation

#### `swimming_team_rankings()`
- Returns `Rank`, `Team`, `Count`, `Gender`, and `Date` (date data was recorded).

#### `swimming_athlete_rankings()`
- Returns a pandas dataframe with the columns `Season`, `Gender`, `Rank`, `Athlete/University`, `Age`, `Team`, `Conference`, `Date`, `Meet`, `Time`, `FINA`, `Event`, `Date Collected`. For relay events, age is `N/A`.

Example usage:
```Python
from usportspy import swimming_athlete_rankings, swimming_team_rankings

print(swimming_team_rankings())
print(swimming_athlete_rankings())
```

Expected output:
```
     Rank                            Team  Count  Gender        Date
0       1           University Of Toronto    585    Male  31/05/2024
1       2  University Of British Columbia    485    Male  31/05/2024
2       3   University Of Calgary Varsity    409    Male  31/05/2024
3       4               McGill University    309    Male  31/05/2024
4       5            University Of Ottawa    210    Male  31/05/2024
..    ...                             ...    ...     ...         ...
111    23      Wilfrid Laurier University      0  Female  26/06/2024
112    23                  Upei Swim Club      0  Female  26/06/2024
113    23                UNB Varsity Reds      0  Female  26/06/2024
114    23    Memorial University Seahawks      0  Female  26/06/2024
115    23             Carleton University      0  Female  26/06/2024

[116 rows x 5 columns]
          Season  Gender  Rank  ... FINA             Event Date Collected
0      2007-2008    Male     1  ...  815           50 Free     27/06/2024
1      2007-2008    Male     2  ...  809           50 Free     27/06/2024
2      2007-2008    Male     3  ...  783           50 Free     27/06/2024
3      2007-2008    Male     4  ...  765           50 Free     27/06/2024
4      2007-2008    Male     5  ...  760           50 Free     27/06/2024
...          ...     ...   ...  ...  ...               ...            ...
29709  2023-2024  Female    24  ...  566  400 Medley Relay     27/06/2024
29710  2023-2024  Female    25  ...  557  400 Medley Relay     27/06/2024
29711  2023-2024  Female    26  ...  530  400 Medley Relay     27/06/2024
29712  2023-2024  Female    27  ...  489  400 Medley Relay     27/06/2024
29713  2023-2024  Female    28  ...  405  400 Medley Relay     27/06/2024

[29714 rows x 13 columns]
```


## Track and Field Documentation

#### tnf_athlete_rankings()
- Returns individual rankings for specific events in a season.


#### tnf_team_rankings()


#### tnf_rosters()


#### tnf_meet_results()


#### tnf_universities()


Example usage:
```Python
from usportspy import tnf_athlete_rankings, tnf_team_rankings, tnf_rosters, tnf_meet_results, tnf_universities 

print(tnf_athlete_rankings())
print(tnf_team_rankings())
print(tnf_rosters())
print(tnf_meet_results())
print(tnf_universities())

```


Expected output:
```
      Rank         Athlete Name                                      Athlete Link University Performance  YOE  ... Placement        Date Gender     Season       Event        Recorded Date
0        1      Kieran Johnston        /usports/tnf/athletes/kieran-johnston/952/       SASK        6.28  2.0  ...       NaN  01/25/2018    men  2017/2018    50-meter  07/19/2024-22:21:14
1        1        Karson Lehner         /usports/tnf/athletes/karson-lehner/7366/       SASK        6.06  2.0  ...        10  01/24/2019    men  2018/2019    50-meter  07/19/2024-22:21:14
2        1  Usheoritse Itsekiri  /usports/tnf/athletes/usheoritse-itsekiri/12080/       REGI        5.75  1.0  ...       NaN  01/27/2023    men  2022/2023    50-meter  07/19/2024-22:21:14
3        2       Storm Zablocki       /usports/tnf/athletes/storm-zablocki/12310/       REGI        5.82  1.0  ...       NaN  01/27/2023    men  2022/2023    50-meter  07/19/2024-22:21:14
4        3         Jordan Soufi         /usports/tnf/athletes/jordan-soufi/10383/       MANI        5.87  3.0  ...         3  01/27/2023    men  2022/2023    50-meter  07/19/2024-22:21:14
...    ...                  ...                                               ...        ...         ...  ...  ...       ...         ...    ...        ...         ...                  ...
44231   42       Francis Latour       /usports/tnf/athletes/francis-latour/10300/       LAVA     3437pts  2.0  ...        17  12/07/2024  women  2023/2024  heptathlon  07/19/2024-22:21:14
44232   43         Ethan Foster         /usports/tnf/athletes/ethan-foster/10641/       TRIN     3239pts  3.0  ...       NaN  01/19/2024  women  2023/2024  heptathlon  07/19/2024-22:21:14
44233   44     Yannick Boudreau     /usports/tnf/athletes/yannick-boudreau/10047/       MONC     3231pts  3.0  ...         1  02/02/2024  women  2023/2024  heptathlon  07/19/2024-22:21:14
44234   45         Zev Zabitsky         /usports/tnf/athletes/zev-zabitsky/13410/       YORK     2998pts  1.0  ...       NaN  02/02/2024  women  2023/2024  heptathlon  07/19/2024-22:21:14
44235   46             Alex Fou             /usports/tnf/athletes/alex-fou/13752/       MCGI     2813pts  1.0  ...       NaN  12/08/2024  women  2023/2024  heptathlon  07/19/2024-22:21:14

[44236 rows x 14 columns]
       Season Gender  Ranking           School     PTS        Recorded Date
0   2023/2024    Men        1          Western   93.33  07/19/2024-23:15:02
1   2023/2024    Men        2           Guelph   92.00  07/19/2024-23:15:02
2   2023/2024    Men        3         Manitoba   83.33  07/19/2024-23:15:02
3   2023/2024    Men        4          Alberta   57.50  07/19/2024-23:15:02
4   2023/2024    Men        5            Laval   53.00  07/19/2024-23:15:02
5   2023/2024    Men        6          Windsor   34.00  07/19/2024-23:15:02
6   2023/2024    Men        7          Toronto   31.00  07/19/2024-23:15:02
7   2023/2024    Men        8           Regina   29.00  07/19/2024-23:15:02
8   2023/2024    Men        9          Calgary   26.50  07/19/2024-23:15:02
9   2023/2024    Men       10  Trinity Western   19.50  07/19/2024-23:15:02
10  2023/2024  Women        1          Western  120.50  07/19/2024-23:15:02
11  2023/2024  Women        2           Guelph  118.50  07/19/2024-23:15:02
12  2023/2024  Women        3     Saskatchewan   96.00  07/19/2024-23:15:02
13  2023/2024  Women        4          Calgary   75.50  07/19/2024-23:15:02
14  2023/2024  Women        5            Laval   62.00  07/19/2024-23:15:02
15  2023/2024  Women        6          Toronto   30.00  07/19/2024-23:15:02
16  2023/2024  Women        6          Alberta   30.00  07/19/2024-23:15:02
17  2023/2024  Women        8          Windsor   24.50  07/19/2024-23:15:02
18  2023/2024  Women        9         Manitoba   16.00  07/19/2024-23:15:02
19  2023/2024  Women       10           Regina   15.00  07/19/2024-23:15:02
                      School              Name Sex Birthday                          Program/Position  Eligibility            Hometown     Type        Recorded Date
0           Brock University     Spencer House   M      NaN                                     Coach          NaN           Saskatoon  Support  07/19/2024-22:33:56
1           Brock University       Kevin Moore   M      NaN                           Assistant Coach          NaN  St. Catharines, ON  Support  07/19/2024-22:33:56
2           Brock University    Morris Agyeman   M     2005                                       NaN          1.0                 NaN  Athlete  07/19/2024-22:33:56
3           Brock University  Andrew Armstrong   M     1982  PhD Behavioural & Cognitive Neuroscience          NaN         Thorold, ON  Athlete  07/19/2024-22:33:56
4           Brock University  Khalifa Badamasi   M     1992                        General Humanities          NaN      Abuja, Nigeria  Athlete  07/19/2024-22:33:56
...                      ...               ...  ..      ...                                       ...          ...                 ...      ...                  ...
2705  University of Victoria     Emma Riendeau   F     2003                               Engineering          1.0       Saskatoon, SK  Athlete  07/19/2024-22:33:56
2706  University of Victoria    Kallalei Ryden   F     2002                                   Science          1.0         Gibsons, BC  Athlete  07/19/2024-22:33:56
2707  University of Victoria  Sophie Sigfstead   F     2000                                   Science          1.0        Edmonton, AB  Athlete  07/19/2024-22:33:56
2708  University of Victoria    Anabelle Traub   F     2003                                   Science          1.0        Edmonton, AB  Athlete  07/19/2024-22:33:56
2709  University of Victoria      Ilona Zrinyi   F     2002                               Engineering          1.0            Winnipeg  Athlete  07/19/2024-22:33:56

[2710 rows x 9 columns]
                       Date                               Name            Location                                         Results
0                03/01/1975          OUAA Indoor Championships         Toronto, ON        /results/ouaa-indoor-championships/2530/
1     02/28/1975-03/01/1975         CWUAA Indoor Championships                  SK       /results/cwuaa-indoor-championships/2474/
2                02/14/1975  OUAA Indoor Championships (paper)         Toronto, ON  /results/ouaa-indoor-championships-paper/2531/
3                02/28/1974          OUAA Indoor Championships                  ON        /results/ouaa-indoor-championships/2450/
4                02/27/1974               OUAA Indoor Rankings                  ON             /results/ouaa-indoor-rankings/2451/
...                     ...                                ...                 ...                                             ...
1161             01/20/2024          Don Wright Team Challenge     London, Ontario        /results/don-wright-team-challenge/9560/
1162  01/19/2024-01/20/2024                        Winter Open  Winnipeg, Manitoba                      /results/winter-open/9559/
1163  01/12/2024-01/13/2024                  Sanderson Classic         Saskatoon,                 /results/sanderson-classic/9544/
1164             01/07/2024                  JACK SIMPSON OPEN    CALGARY, Alberta                /results/jack-simpson-open/9532/
1165             01/06/2024      2024 Sharon Anderson Memorial    Toronto, Ontario    /results/2024-sharon-anderson-memorial/9528/

[1166 rows x 4 columns]
                                     School                       Conference                                               Link
0                          Brock University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
1                       Lakehead University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
2                     Laurentian University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
3                       McMaster University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
4                      Nipissing University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
5                        Queen's University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
6                    Royal Military College     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
7                 Toronto Metropolitan Bold     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
8                          Trent University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
9                      University of Guelph     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
10                     University of Ottawa     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
11                    University of Toronto     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
12                   University of Waterloo     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
13                    University of Windsor     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
14                       Western University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
15                          Wilfrid Laurier     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
16                          York University     Ontario University Athletics  https://www.trackie.com/usports/tnf/universiti...
17                        Acadia University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
18                   Cape Breton University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
19                     Dalhousie University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
20                      Memorial University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
21                 Mount Allison University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
22                  Saint Mary's University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
23            St. Francis Xavier University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
24                    St. Thomas University        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
25                    Université de Moncton        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
26              University of New Brunswick        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
27       University of Prince Edward Island        Atlantic University Sport  https://www.trackie.com/usports/tnf/universiti...
28                      Carleton University  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
29                     Concordia University  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
30          École de technologie supérieure  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
31                        McGill University  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
32              Université à Trois-Rivières  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
33                   Université de Montréal  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
34                 Université de Sherbrooke  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
35                         Université Laval  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
36                            UQÀM Citadins  Quebec Student Sport Federation  https://www.trackie.com/usports/tnf/universiti...
37               Trinity Western University                      Canada West  https://www.trackie.com/usports/tnf/universiti...
38                    University of Alberta                      Canada West  https://www.trackie.com/usports/tnf/universiti...
39           University of British Columbia                      Canada West  https://www.trackie.com/usports/tnf/universiti...
40  University of British Columbia Okanagan                      Canada West  https://www.trackie.com/usports/tnf/universiti...
41                    University of Calgary                      Canada West  https://www.trackie.com/usports/tnf/universiti...
42                 University of Lethbridge                      Canada West  https://www.trackie.com/usports/tnf/universiti...
43                   University of Manitoba                      Canada West  https://www.trackie.com/usports/tnf/universiti...
44                     University of Regina                      Canada West  https://www.trackie.com/usports/tnf/universiti...
45               University of Saskatchewan                      Canada West  https://www.trackie.com/usports/tnf/universiti...
46                   University of Victoria                      Canada West  https://www.trackie.com/usports/tnf/universiti...
```


 -->
