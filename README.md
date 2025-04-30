# is477-sp25-group3
Jon Han &amp; Faris Hammad

Metadeta:

Project Title & Overview - 
Our project aimed to answer the research question "What is the correlation between offensive rebounds and probability of winning?"
It used an "NBA Database" which included data on all 30 NBA teams, as well as over 4,800 players and 65,000 games. There are box scores for over 95% of all of these games, as well as play-by-play game data with 13M+ rows of data. (https://www.kaggle.com/datasets/wyattowalsh/basketball) It also used an "NBA Players" which contained over two decades of data on each player who has been a part of an NBA roster. It includes demographic variables such as age, height, weight, place of birth, and other details such as team played for, draft year, and round. Additionally, it also contains basic box score statistics such as games played, average number of points, rebounds, and assists. (https://www.kaggle.com/datasets/justinas/nba-players-data)

Citation - 
To cite this project, use the following DOI: 
10.5281/zenodo.15253192
Zenodo DOI: [![DOI](https://zenodo.org/badge/946780081.svg)](https://doi.org/10.5281/zenodo.15253191)

Requirements & Dependencies - 
Software:
Snakemake (version 9.3.0)
Python (version 3.13.3)
Libraries:
pandas (version 2.2.3) https://pandas.pydata.org/
matplotlib (version3.10.1) https://matplotlib.org/
seaborn (0.13.2) https://seaborn.pydata.org/

Installations:
How to install and set up the environment:
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

All Data Sources:
Datasets - 
Wyatt Walsh. "Basketball Dataset". Kaggle, https://www.kaggle.com/datasets/wyattowalsh/basketball.
Justinas. "NBA Players Data". Kaggle, https://www.kaggle.com/datasets/justinas/nba-players-data.
Software - 
Snakemake. "Snakemake: a scalable bioinformatics workflow engine". https://snakemake.readthedocs.io/.
Libraries - 
pandas (version 2.2.3) https://pandas.pydata.org/
matplotlib (version3.10.1) https://matplotlib.org/
seaborn (0.13.2) https://seaborn.pydata.org/

Full Project Report:

Title: "What is the correlation between offensive rebounds and probability of winning?"

Link to archival record: 10.5281/zenodo.15253192
Zenodo DOI - [![DOI](https://zenodo.org/badge/946780081.svg)](https://doi.org/10.5281/zenodo.15253191)

Contributors: Jon Han & Faris Hammad

Summary: This project will dive into two different aspects of what would essentially make a successful and efficient basketball team. In this project, we will use historical player data as well as identify trends, primarily associated with how effective offensive rebounds can be in winning individual games. This data will hopefully help us to best answer our research question which was "What is the correlation between offensive rebounds and probability of winning?". Additionally, perhaps offer new insights to long-term NBA fans through statistically significant data that the fans may have otherwise seldom considered. We found that there is a very moderate correlation between more offensive rebounds and probability of winning. We visualized this on a graph, and ultimately determined that the correlation between the two was incredibly moderate, if any, and not very significant. 

Data profile: These were our datasets and data sources that we used: Datasets - 
Wyatt Walsh. "Basketball Dataset". Kaggle, https://www.kaggle.com/datasets/wyattowalsh/basketball.
Justinas. "NBA Players Data". Kaggle, https://www.kaggle.com/datasets/justinas/nba-players-data.
Software - 
Snakemake. "Snakemake: a scalable bioinformatics workflow engine". https://snakemake.readthedocs.io/.
Libraries - 
pandas (version 2.2.3) https://pandas.pydata.org/
matplotlib (version3.10.1) https://matplotlib.org/
seaborn (0.13.2) https://seaborn.pydata.org/. The "Basketball Dataset" included data on all 30 NBA teams, as well as over 4,800 players and 65,000 games. There are box scores for over 95% of all of these games, as well as play-by-play game data with 13M+ rows of data. As for the "NBA Players Data" dataset, it contained over two decades of data on each player who has been a part of an NBA roster. It includes demographic variables such as age, height, weight, place of birth, and other details such as team played for, draft year, and round. Additionally, it also contains basic box score statistics such as games played, average number of points, rebounds, and assists. 

Findings: We visulized our findings through two visualizations, offensive_rebound_vs_net_rating.png and offensive_rebound_vs_points_per_game.png. Offensive_rebound_vs_net_rating.png compares offensive rebound percentage and a team's net rating which essentially is supposed to reflect how good a team is / how likely they are to win. The data is very dense near 0-0.2 offensive rebound percentages and net ratings between -50 and +50. There are a few outliers, but overall there is no strong upward or downward trend. This suggests that there is not a very strong correlation between the two. Offensive_rebound_vs_points_per_game.png compares offensive rebound percentage and points per game which is a strong indicator for team will win, because the team with more points wins the game. We found that most high point scorers have low offensive rebound rates. This makes sense because players focused on scoring the ball are not as focused on chasing after offensive rebounds. This shows that offensive rebounds are inversely correlated with individual scoring and also represents the importance of role specialization. Because offensive rebounds are inversely correlated with individual scoring and total points, it also reflects a weak correlation between offensive rebounds and winning games. While both points and offensive rebounds are factors to win games, them having an inverse correlation shows that they are not very relevant and correlated to each other. 

Future Work: We learned a few different lessons. Firstly, data integration is rarely seamless. There are so many different factors like capitalizations, spaces, and punctation which can make data integration an incredibly difficult process. Additionally, we learned that data reproducaiblity adds long-term value. It ensures that projects and data can be reliably be rerun, updated, and analyzed by others. There are also a few ideas for future work that we could implement or utilize. Firstly, other advanced statistics could be implemented or utilized to give a clearer picture. If we also considered something like the amount of defensive rebounds per game or the amount of all star players on a team, we could have had a more multifaceted viewpoint of offensive rebounds. Additionally, another idea for future work is examining if trends in offensive rebounds and winning games changed historically. It might be interesting to see if there was a stronger or weaker correlation in the past compared to the present. 

Reproducing:
1. Set up project directory
nba-project/
├── data/                         # Raw input data
│   ├── NBA_players_data.csv
│   ├── NBA_stats_data.csv
├── outputs/                      # Final outputs (auto-generated)
├── scripts/                      # Python scripts
│   ├── clean_and_merge.py
│   ├── analyze_and_plot.py
│   ├── create_log.py
├── Snakefile                     # Snakemake workflow
├── environment.yml               # Reproducible environment (optional)

2. Set up environment
name: nba_env
dependencies:
  - python=3.10
  - pandas
  - seaborn
  - matplotlib
  - snakemake
conda env create -f environment.yml
conda activate nba_env

3. Download and place datasets
Place dataset files into the data/ folder

4. Write the snakemake workflow
rule all:
    input:
        "outputs/offensive_rebound_vs_points_per_game.png",
        "outputs/offensive_rebound_vs_net_rating.png",
        "outputs/log.txt"
rule clean_and_merge:
    input:
        stats_data="data/NBA_stats_data.csv",
        player_info="data/NBA_players_data.csv"
    output:
        "outputs/merged_player_data.csv"
    script:
        "scripts/clean_and_merge.py"
rule analyze_and_plot:
    input:
        "outputs/merged_player_data.csv"
    output:
        "outputs/offensive_rebound_vs_points_per_game.png",
        "outputs/offensive_rebound_vs_net_rating.png"
    script:
        "scripts/analyze_and_plot.py"
rule create_log:
    input:
        "outputs/merged_player_data.csv"
    output:
        "outputs/log.txt"
    script:
        "scripts/create_log.py"

5. Clean and merge the data
import pandas as pd
def clean_name(name):
    return name.strip().lower().replace('.', '').replace(',', '')
stats_df = pd.read_csv("data/NBA_stats_data.csv")
player_info_df = pd.read_csv("data/NBA_players_data.csv")
stats_df['player_clean'] = stats_df['player_name'].apply(clean_name)
player_info_df['player_clean'] = player_info_df['full_name'].apply(clean_name)
player_info_df.drop_duplicates(subset='player_clean', inplace=True)
merged_df = pd.merge(stats_df, player_info_df, on='player_clean', how='left')
merged_df.drop(columns=['player_clean'], inplace=True)
merged_df.to_csv("outputs/merged_player_data.csv", index=False)

6. Analyze and visualize the data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("outputs/merged_player_data.csv")
# Plot 1: ORB% vs Points Per Game
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='oreb_pct', y='pts', scatter_kws={'alpha': 0.4})
plt.title("Offensive Rebound % vs Points Per Game")
plt.xlabel("Offensive Rebound %")
plt.ylabel("Points Per Game")
plt.tight_layout()
plt.savefig("outputs/offensive_rebound_vs_points_per_game.png")
plt.close()
# Plot 2: ORB% vs Net Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='oreb_pct', y='net_rating', hue='is_active', alpha=0.6)
plt.title("Offensive Rebound % vs Net Rating")
plt.xlabel("Offensive Rebound %")
plt.ylabel("Net Rating")
plt.tight_layout()
plt.savefig("outputs/offensive_rebound_vs_net_rating.png")
plt.close()

7. Create a reproducability log
import pandas as pd
df = pd.read_csv("outputs/merged_player_data.csv")
with open("outputs/log.txt", "w") as f:
    f.write("NBA Data Integration Run Log\n")
    f.write(f"Total Rows in Final Merged Dataset: {len(df)}\n")
    f.write("Missing values after merge:\n")
    f.write(str(df.isnull().sum()))
    f.write("\n\nScript completed successfully.")

8. Run the workflow
snakemake --cores 1

References: All listed above 
