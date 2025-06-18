import pandas as pd
import soccerdata as sd
import numpy as np

years = ['19-20', '20-21', '21-22', '22-23', '23-24', '24-25']

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

x = '19-20'

df = get_standard_data(x)
df.head()
df.shape

# Standard - All 90's - drop GK
# defense - clr, int, shots_blocked, tckl_int, tackles
# sca - all 90's
# misc - aerial_won, fls, fld, recov
# pass - final_third, xAG, CrsPA, PPA, PrgP
# poss - PrgC, CPA
# shot - npxG - account for goalies having no xG
