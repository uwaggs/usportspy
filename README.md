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
- [ ] Swimming
- [ ] Track & Field
- [ ] Cross Country
- [ ] Curling


## Wresling Documentation

#### `wrestling_athlete_rankings(gender, weight)`
- `gender`: can be either `"MALE"` or `"FEMALE"`
- `weight`: an integer representing the weight class to return data for in kilograms.
- Returns a pandas dataframe with the columsn `Weight Category`, `Rank`, `School`, `Last Updated`. 

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
