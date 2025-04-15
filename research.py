import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Automatic (programmatic) integration of datasets using Python/Pandas and/or SQL (cf. Weeks 5-6)
# Document data profiling, quality assessment, and cleaning (cf. Week 7)


# Load datasets
stats_df = pd.read_csv("NBA players/all_seasons.csv")
player_info_df = pd.read_csv("NBA database/csv/player.csv")

# Clean and standardize player names
def clean_name(name):
    return name.strip().lower().replace('.', '').replace(',', '')

stats_df['player_clean'] = stats_df['player_name'].apply(clean_name)
player_info_df['player_clean'] = player_info_df['full_name'].apply(clean_name)

# Data profiling
print("\n=== Data Profiling ===")
print("Stats Dataset Overview:")
print(stats_df.info())
print(stats_df.describe(include='all'))
print(f"Unique players in stats_df: {stats_df['player_name'].nunique()}")

print("\nPlayer Info Dataset Overview:")
print(player_info_df.info())
print(player_info_df.describe(include='all'))
print(f"Unique players in player_info_df: {player_info_df['full_name'].nunique()}")

# Quality assessment
print("\n=== Quality Assessment ===")
print("Missing values in stats_df:\n", stats_df.isnull().sum())
print("Missing values in player_info_df:\n", player_info_df.isnull().sum())

# Check for duplicates
duplicates = player_info_df.duplicated(subset='player_clean').sum()
print(f"Duplicate cleaned player names in player_info_df: {duplicates}")

unmatched_names = stats_df[~stats_df['player_clean'].isin(player_info_df['player_clean'])]
print(f"Unmatched player names (will have NaNs after merge): {len(unmatched_names)}")

# Data cleaning
print("\n=== Cleaning Data ===")
player_info_df.drop_duplicates(subset='player_clean', inplace=True)

# Merge datasets
merged_df = pd.merge(stats_df, player_info_df, on='player_clean', how='left')
merged_df.drop(columns=['player_clean'], inplace=True)
merged_df.to_csv("merged_player_data.csv", index=False)

print("Merge complete! Final rows:", len(merged_df))


# Implement simple data analysis and/or visualization (answering at least part of your RQs)
# Create a reproducible package (cf. Week 8)


# Image: Offensive rebound % vs Points per Game 
plt.figure(figsize=(10, 6))
sns.regplot(data=merged_df, x='oreb_pct', y='pts', scatter_kws={'alpha': 0.4})
plt.title("Offensive Rebound % vs Points Per Game")
plt.xlabel("Offensive Rebound %")
plt.ylabel("Points Per Game")
plt.tight_layout()
plt.savefig("offensive_rebound_vs_points_per_game.png")
plt.close()

# Image: Offensive rebound % vs Win Proxy (e.g., Net Rating)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='oreb_pct', y='net_rating', hue='is_active', alpha=0.6)
plt.title("Offensive Rebound % vs Net Rating")
plt.xlabel("Offensive Rebound %")
plt.ylabel("Net Rating")
plt.tight_layout()
plt.savefig("offensive_rebound_vs_net_rating.png")
plt.close()

# Signals successful script completion and prints the output artifacts so it’s easier to verify in a reproducible setting
if __name__ == "__main__":
    print("\n Script finished successfully. All outputs saved.")
    print("📁 Outputs:")
    print(" - merged_player_data.csv")
    print(" - offensive_rebound_vs_points_per_game.png")
    print(" - offensive_rebound_vs_net_rating.png")

# Create a reproducability log file
with open("log.txt", "w") as f:
    f.write("NBA Data Integration Run Log\n")
    f.write("Total Rows in Final Merged Dataset: {}\n".format(len(merged_df)))
    f.write("Missing values after merge:\n")
    f.write(str(merged_df.isnull().sum()))
    f.write("\n\nScript completed successfully.")