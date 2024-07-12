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
