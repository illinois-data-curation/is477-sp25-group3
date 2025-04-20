# Rule to download the datasets
rule download_datasets:
    output:
        "NBA_players_data.csv",
        "NBA_stats_data.csv"
    shell:
        """
        # Use wget or curl to download the datasets from Kaggle (ensure proper API token setup)
        kaggle datasets download -d wyattowalsh/basketball -p ./data
        kaggle datasets download -d justinas/nba-players-data -p ./data
        """

# Rule to clean and merge the datasets
rule clean_and_merge:
    input:
        stats_data="NBA_stats_data.csv",
        player_info="NBA_players_data.csv"
    output:
        "merged_player_data.csv"
    script:
        "scripts/clean_and_merge.py"

# Rule to analyze and plot data
rule analyze_and_plot:
    input:
        "merged_player_data.csv"
    output:
        "offensive_rebound_vs_points_per_game.png",
        "offensive_rebound_vs_net_rating.png"
    script:
        "scripts/analyze_and_plot.py"

# Rule to create a reproducibility log
rule create_log:
    input:
        "merged_player_data.csv"
    output:
        "log.txt"
    script:
        "scripts/create_log.py"

# Default rule to run everything
rule all:
    input:
        "offensive_rebound_vs_points_per_game.png",
        "offensive_rebound_vs_net_rating.png",
        "log.txt"