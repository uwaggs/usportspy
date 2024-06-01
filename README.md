# USPORTSPY - One-Stop-Shop for USPORTS Data

## Disclaimer
This package is still early in development, and is subject to unexpected changes. If you'd still like to try this out, be sure to only use the latest package.

## Included Sports
- [X] [Wrestling](https://github.com/uwaggs/wrestling)
- [ ] Volleyball
- [ ] Basketball
- [ ] Ice Hockey
- [ ] Soccer
- [ ] Rugby
- [ ] Field Hockey
- [ ] Football
- [X] [Swimming](https://github.com/uwaggs/swimming)
- [ ] Track & Field
- [ ] Cross Country
- [ ] Curling


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
   Weight Category Rank                 School Last Updated
0             57kg    1          Kyle Robinson   02/01/2020
1             57kg    2       Garette Saunders   02/01/2020
2             57kg    3          Harris Valdes   02/01/2020
3             57kg    4         Drake Buechler   02/01/2020
4             57kg    5      Francesco Fortino   02/01/2020
..             ...  ...                    ...          ...
60            57kg    4             Lucas Reid   01/30/2024
61            57kg    5        Gabe Sementilli   01/30/2024
62            57kg    6          Fred Calingay   01/30/2024
63            57kg    7        Sullivan Valdez   01/30/2024
64            57kg    8  Edward Matida-Torrico   01/30/2024

[65 rows x 4 columns]
   Weight Category  Rank             School Last Updated
0             56kg     1    Alexandria Town   11/16/2021
1             56kg     2      SueAnne Harms   11/16/2021
2             56kg     3        Vivica Addo   11/16/2021
3             56kg     4     Grace Chambers   11/16/2021
4             56kg     5      Macy Malysiak   11/16/2021
5             56kg     6    Daina Armstrong   11/16/2021
6             56kg     1      SueAnne Harms   11/22/2021
7             56kg     2    Alexandria Town   11/22/2021
8             56kg     3      Macy Malysiak   11/22/2021
9             56kg     4        Vivica Addo   11/22/2021
10            56kg     5     Grace Chambers   11/22/2021
11            56kg     6     Emalea Drozdow   11/22/2021
12            56kg     1      Macy Malysiak   10/31/2022
13            56kg     2  Robbie Ann Pingal   10/31/2022
14            56kg     3     Gabriela Cross   10/31/2022
15            56kg     4      Jayden Sparks   10/31/2022
16            56kg     5      Allison Kuzub   10/31/2022
17            56kg     1  Robbie Ann Pingal   01/30/2023
18            56kg     2    Virginie Gascon   01/30/2023
19            56kg     3      Macy Malysiak   01/30/2023
20            56kg     4      Jayden Sparks   01/30/2023
21            56kg     5       Alison Kuzub   01/30/2023
22            56kg     6     Emalea Drozdow   01/30/2023
23            56kg     7        Ella Jakobi   01/30/2023
24            56kg     8     Gabriela Cross   01/30/2023
25            56kg     1        Mia Friesen   02/14/2023
26            56kg     2    Virginie Gascon   02/14/2023
27            56kg     3     Gabriela Cross   02/14/2023
28            56kg     4  Robbie Ann Pingal   02/14/2023
29            56kg     5       Alison Kuzub   02/14/2023
30            56kg     6      Macy Malysiak   02/14/2023
31            56kg     7      Jayden Sparks   02/14/2023
32            56kg     8       Kirti Saxena   02/14/2023
33            56kg     1      SueAnne Harms   12/05/2023
34            56kg     2        Anika Fines   12/05/2023
35            56kg     3    Virginie Gascon   12/05/2023
36            56kg     4     Brooklyn Brown   12/05/2023
37            56kg     5  Robbie Ann Pingal   12/05/2023
38            56kg     6   Kendall Dettloff   12/05/2023
39            56kg     7      Jayden Sparks   12/05/2023
40            56kg     8        Mayumi King   12/05/2023
41            56kg     1      SueAnne Harms   01/16/2024
42            56kg     2       Annika Fines   01/16/2024
43            56kg     3     Sophia Bechard   01/16/2024
44            56kg     4   Kendall Dettloff   01/16/2024
45            56kg     5  Robbie Ann Pingal   01/16/2024
46            56kg     6     Brooklyn Brown   01/16/2024
47            56kg     7      Jayden Sparks   01/16/2024
48            56kg     8        Mayumi King   01/16/2024
49            56kg     1      SueAnne Harms   01/30/2024
50            56kg     2       Annika Fines   01/30/2024
51            56kg     3     Sophia Bechard   01/30/2024
52            56kg     4   Kendall Dettloff   01/30/2024
53            56kg     5  Robbie Ann Pingal   01/30/2024
54            56kg     6     Brooklyn Brown   01/30/2024
55            56kg     7      Jayden Sparks   01/30/2024
56            56kg     8        Mayumi King   01/30/2024
```



## Swimming Documentation

#### `swimming_team_rankings()`
- Returns `Rank`, `Team`, `Count`, `Gender`, and `Date` (date data was recorded).

#### `swimming_athlete_rankings()`
- Returns a pandas dataframe with the columns `Rank`, `Athlete/University`, `Age`, `Team`, `Conference`, `Date`, `Meet`, `Time`, `FINA`, and `Event`. For relay events, age is `N/A`.

Example usage:
```Python
from usportspy import swimming_athlete_rankings, swimming_team_rankings

print(swimming_team_rankings())
print(swimming_athlete_rankings())
```

Expected output:
```
    Rank                                     Team  Count  Gender        Date
0      1                    University Of Toronto    585    Male  31/05/2024
1      2           University Of British Columbia    485    Male  31/05/2024
2      3            University Of Calgary Varsity    409    Male  31/05/2024
3      4                        McGill University    309    Male  31/05/2024
4      5                     University Of Ottawa    210    Male  31/05/2024
5      6  University Of Alberta Varsity Swim Team    168    Male  31/05/2024
6      7              WESTERN UNIVERSITY SWIMMING    117    Male  31/05/2024
7      8                   University Of Waterloo    107    Male  31/05/2024
8      9                 University Of Lethbridge     84    Male  31/05/2024
9     10                      McMaster University     73    Male  31/05/2024
10    11                     UVIC VIKES Swim Team     71    Male  31/05/2024
11    12                          York University     59    Male  31/05/2024
12    13              Dalhousie University Tigers     49    Male  31/05/2024
13    14             Memorial University Seahawks     48    Male  31/05/2024
14    15               Wilfrid Laurier University     45    Male  31/05/2024
15    16                Rouge et Or Universitaire     31    Male  31/05/2024
16    17                      Carleton University     22    Male  31/05/2024
17    18                   UNIVERSITE DE MONTREAL     20    Male  31/05/2024
18    19                        Acadia University     15    Male  31/05/2024
19    20                 UNIVERSITE DE SHERBROOKE     12    Male  31/05/2024
20    21    UNIVERSITE DU QUEBEC A TROIS-RIVIERES      8    Male  31/05/2024
21    21               Brock University Swim Club      8    Male  31/05/2024
22    23   University Of Manitoba Bisons Swimming      7    Male  31/05/2024
23    24                     University Of Guelph      4    Male  31/05/2024
24    24                   Mount Allison Mounties      4    Male  31/05/2024
25    26                         UNB Varsity Reds      2    Male  31/05/2024
26    27              Queens University Swim Club      0    Male  31/05/2024
27    27                           Upei Swim Club      0    Male  31/05/2024
28    27     University Of Regina Cougar Swimming      0    Male  31/05/2024
29     1           University Of British Columbia    842  Female  31/05/2024
30     2                    University Of Toronto    660  Female  31/05/2024
31     3            University Of Calgary Varsity    381  Female  31/05/2024
32     4                        McGill University    329  Female  31/05/2024
33     5              WESTERN UNIVERSITY SWIMMING    123  Female  31/05/2024
34     6                   UNIVERSITE DE MONTREAL     90  Female  31/05/2024
35     7                        Acadia University     81  Female  31/05/2024
36     8                 University Of Lethbridge     73  Female  31/05/2024
37     9   University Of Manitoba Bisons Swimming     59  Female  31/05/2024
38    10                      McMaster University     58  Female  31/05/2024
39    11                   University Of Waterloo     56  Female  31/05/2024
40    12              Dalhousie University Tigers     50  Female  31/05/2024
41    13                     UVIC VIKES Swim Team     48  Female  31/05/2024
42    14  University Of Alberta Varsity Swim Team     24  Female  31/05/2024
43    15                Rouge et Or Universitaire     22  Female  31/05/2024
44    16               Brock University Swim Club     20  Female  31/05/2024
45    17                 UNIVERSITE DE SHERBROOKE     14  Female  31/05/2024
46    18                     University Of Guelph      8  Female  31/05/2024
47    19                     University Of Ottawa      7  Female  31/05/2024
48    20              Queens University Swim Club      4  Female  31/05/2024
49    21                   Mount Allison Mounties      3  Female  31/05/2024
50    22     University Of Regina Cougar Swimming      1  Female  31/05/2024
51    23                          York University      0  Female  31/05/2024
52    23    UNIVERSITE DU QUEBEC A TROIS-RIVIERES      0  Female  31/05/2024
53    23               Wilfrid Laurier University      0  Female  31/05/2024
54    23                           Upei Swim Club      0  Female  31/05/2024
55    23                         UNB Varsity Reds      0  Female  31/05/2024
56    23             Memorial University Seahawks      0  Female  31/05/2024
57    23                      Carleton University      0  Female  31/05/2024
       Rank                     Athlete/University  ...  FINA             Event
0         1                          Forde, Martyn  ...   815           50 Free
1         2                       Haynes, Terrence  ...   809           50 Free
2         3                             Ng, Callum  ...   783           50 Free
3         4                         Anctil, Pascal  ...   765           50 Free
4         5                      Savoie, Alexandre  ...   760           50 Free
...     ...                                    ...  ...   ...               ...
29709    24                       UNB Varsity Reds  ...   566  400 Medley Relay
29710    25   University Of Regina Cougar Swimming  ...   557  400 Medley Relay
29711    26  UNIVERSITE DU QUEBEC A TROIS-RIVIERES  ...   530  400 Medley Relay
29712    27                    Carleton University  ...   489  400 Medley Relay
29713    28                        York University  ...   405  400 Medley Relay

[29714 rows x 10 columns]
```
