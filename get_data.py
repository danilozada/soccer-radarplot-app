# Libraries
import pandas as pd
import soccerdata as sd
import numpy as np
from functools import reduce

# Seasons
years = ['20-21', '21-22', '22-23', '23-24', '24-25']

# Standard data
def get_standard_data(year):
    
    # Desired columns from standard data
    standard_cols = [
    ('league', ''),
    ('season', ''),
    ('team', ''),
    ('pos', ''),
    ('player', ''),
    ('age', ''),
    ('Playing Time', 'MP'),
    ('Playing Time', '90s')
    ]
    # Get standard data
    standard_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=year).read_player_season_stats('standard').reset_index()
    
    # Filter by desired columns
    standard_df = standard_df.loc[:, standard_cols]

    # Set new columns names
    new_standard_cols = ['league', 'season', 'team', 'pos', 'player', 'age', 'matches', '90s']
    standard_df.columns = new_standard_cols

    return(standard_df)

# Defense data
def get_defense_data(year):
    
    # Desired columns from defensive data
    defense_cols = [
    ('league', ''),
    ('season', ''),
    ('team', ''),
    ('player', ''),
    ('Clr', ''),
    ('Challenges', 'Tkl%'),
    ('Int', ''),
    ('Blocks', 'Sh'),
    ('Tkl+Int', ''),
    ('Challenges', 'Tkl'),

    ]
    # Get defensive data
    defense_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=year).read_player_season_stats('defense').reset_index()
    
    # Filter by desired columns
    defense_df = defense_df.loc[:, defense_cols]

    # Set new columns names
    new_defense_cols = ['league', 'season', 'team', 'player', 'clearances', 'tackle_perc', 'int', 
                        'shots_blocked', 'tkl_int', 'tackles']
    defense_df.columns = new_defense_cols

    return(defense_df)

# SCA data
def get_sca_data(year):
    
    # Desired columns from SCA data
    sca_cols = [
    ('league', ''),
    ('season', ''),
    ('team', ''),
    ('player', ''),
    ('SCA', 'SCA90')
    ]
    
    # Get SCA data
    sca_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=year).read_player_season_stats('goal_shot_creation').reset_index()
    
    # Filter by desired columns
    sca_df = sca_df.loc[:, sca_cols]

    # Set new columns names
    new_sca_cols = ['league', 'season', 'team', 'player', 'sca']
    sca_df.columns = new_sca_cols

    return(sca_df)

# Misc data
def get_misc_data(year):
    
    # Desired columns from misc data
    misc_cols = [
    ('league', ''),
    ('season', ''),
    ('team', ''),
    ('player', ''),
    ('Aerial Duels', 'Won'),
    ('Aerial Duels', 'Won%'),
    ('Performance', 'Fls'),
    ('Performance', 'Fld'),
    ('Performance', 'Recov')

    ]
    
    # Get misc data
    misc_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=year).read_player_season_stats('misc').reset_index()
    
    # Filter by desired columns
    misc_df = misc_df.loc[:, misc_cols]

    # Set new columns names
    new_misc_cols = ['league', 'season', 'team', 'player', 'aerial_won', 'aerial_perc', 'fls', 'fld', 'recov']
    misc_df.columns = new_misc_cols

    return(misc_df)

# Pass data
def get_pass_data(year):
    
    # Desired columns from pass data
    pass_cols = [
    ('league', ''),
    ('season', ''),
    ('team', ''),
    ('player', ''),
    ('Total', 'Cmp%'),
    ('Long', 'Cmp%'),
    ('1/3', ''),
    ('xAG', ''),
    ('CrsPA', ''),
    ('PPA', ''),
    ('PrgP', '')
    ]
    
    # Get pass data
    pass_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=year).read_player_season_stats('passing').reset_index()
    
    # Filter by desired columns
    pass_df = pass_df.loc[:, pass_cols]

    # Set new columns names
    new_pass_cols = ['league', 'season', 'team', 'player', 'pass_perc', 'long_pass_perc', 'final_third', 
                     'xAG', 'CrsPA', 'PPA', 'PrgP']
    pass_df.columns = new_pass_cols

    return(pass_df)

# Poss data
def get_poss_data(year):
    
    # Desired columns from poss data
    poss_cols = [
    ('league', ''),
    ('season', ''),
    ('team', ''),
    ('player', ''),
    ('Carries', 'PrgC'),
    ('Carries', 'CPA')
    ]
    
    # Get poss data
    poss_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=year).read_player_season_stats('possession').reset_index()
    
    # Filter by desired columns
    poss_df = poss_df.loc[:, poss_cols]

    # Set new columns names
    new_poss_cols = ['league', 'season', 'team', 'player', 'PrgC', 'CPA']
    poss_df.columns = new_poss_cols

    return(poss_df)

# Shot data
def get_shot_data(year):
    
    # Desired columns from shooting data
    shot_cols = [
    ('league', ''),
    ('season', ''),
    ('team', ''),
    ('player', ''),
    ('Expected', 'npxG'),
    ('Standard', 'Sh/90'),
    ('Expected', 'npxG/Sh'),
    ('Standard', 'Dist')
    ]
    
    # Get shooting data
    shot_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=year).read_player_season_stats('shooting').reset_index()
    
    # Filter by desired columns
    shot_df = shot_df.loc[:, shot_cols]

    # Set new columns names
    new_shot_cols = ['league', 'season', 'team', 'player', 'npxG', 'Sh/90', 'npxG/Sh', 'dist']
    shot_df.columns = new_shot_cols

    return(shot_df)

# Combine all data frames
def get_all_data(year):
    year = year
    standard_df = get_standard_data(year)
    defense_df = get_defense_data(year)
    sca_data = get_sca_data(year)
    misc_data = get_misc_data(year)
    pass_data = get_pass_data(year)
    poss_data = get_poss_data(year)
    shot_data = get_shot_data(year)

    all_data = [standard_df, defense_df, sca_data, misc_data, pass_data, poss_data, shot_data]

    df = reduce(lambda left, right: pd.merge(left, right, on = ['league', 'season', 'team', 'player'],
                                             how = 'outer'), all_data)
    
    df = df[df['pos'] != 'GK']
    
    return(df)

# Create blank data frame to append to
all_years_df = pd.DataFrame()

# Loop for different years
for year in years:
    df = get_all_data(year)
    all_years_df = pd.concat([all_years_df, df])
    
# Columns to normalize to 90 minute games
columns_to_normalize = ['clearances', 'int', 'shots_blocked', 'tkl_int', 'tackles', 
                        'aerial_won', 'fls', 'fld', 'recov', 'final_third', 'xAG', 
                        'CrsPA', 'PPA', 'PrgP', 'PrgC', 'CPA', 'npxG']

# Loop for normalize
for c in columns_to_normalize:
    all_years_df[c] = round(all_years_df[c] / all_years_df['90s'],2)

# Fill NA with 0
all_years_df = all_years_df.fillna(0)

# Replace league and season

# league
new_leagues = {'ENG-Premier League' : 'English Premier League', 
           'ESP-La Liga' : 'La Liga',
           'FRA-Ligue 1' : 'Ligue 1',
           'GER-Bundesliga' : 'German Bundesliga',
           'ITA-Serie A' : 'Serie A'}
all_years_df['league'] = all_years_df['league'].replace(new_leagues)

# season
new_seasons = {
               '2021' : '2020/2021', 
               '2122' : '2021/2022', 
               '2223' : '2022/2023', 
               '2324' : '2023/2024', 
               '2425' : '2024/2025'}

all_years_df['season'] = all_years_df['season'].replace(new_seasons)

new_columns = ['league', 'season', 'team', 'pos', 'player', 'age', 'matches', '90s',
       'Clearances', "% of Dribblers Tackled", 'Interceptions', 
       'Shots Blocked', 'Tackles & Interceptions',
       'Tackles', 'Shot Creating Actions', 'Aerial Duels Won', 
       'Aerial Win %', 'Fouls', 'Fouls Drawn', 'Ball Recoveries',
       'Pass Completion %', 'Long Pass Completion %', 'Completed Final Third Passes', 
       'Expected Assisted Goals', 'Crosses into Penalty Area', 'Passes into Penalty Area',
       'Progressive Passes', 'Progressive Carries', 'Carries into Penalty Area', 
       'npxG', 'Shots', 'npxG/Shot', 'Shot Distance (Yards)']

all_years_df.columns = new_columns

all_years_df = all_years_df.reset_index(drop=True)
all_data = all_years_df.fillna(0)
all_data.fillna(0, inplace =True)

# Create csv for app
all_data.to_csv('radar_data.csv', index = False)
