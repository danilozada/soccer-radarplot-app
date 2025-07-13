# radar_function.py
import pandas as pd
import numpy as np
from mplsoccer import Radar, FontManager, grid
import matplotlib.pyplot as plt
from matplotlib import font_manager

URL5 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
        'RobotoSlab%5Bwght%5D.ttf')
robotto_bold = FontManager(URL5)

def get_params(radartype):
    if radartype == 'Centerback':
        params = ['Aerial Duels Won', 'Aerial Win %', 'Pass Completion %',
                'Long Pass Completion %', 'Progressive Carries',
                'Completed Final Third Passes', "% of Dribblers Tackled",
                'Interceptions', 'Shots Blocked', 'Clearances', 'Fouls']
        lower_is_better = ['Fouls']
        radar_position = 'Centerback'    
    if radartype == 'Fullback':
        params = ["% of Dribblers Tackled", 'Progressive Carries', 'Completed Final Third Passes',
          'Crosses into Penalty Area', 'Expected Assisted Goals',
          'Shot Creating Actions', 'Pass Completion %', 'Fouls', 'Aerial Win %', 'Clearances',
          'Tackles & Interceptions']
        lower_is_better = ['Fouls']
        radar_position = 'Fullback'
    if radartype == 'Midfielder':
        params = ['Pass Completion %', 'Progressive Carries', "Progressive Passes",
                  'Expected Assisted Goals', 'Completed Final Third Passes', 
                  "Fouls Drawn", "Fouls", 'Ball Recoveries', 
                  'Interceptions', 'Tackles', "% of Dribblers Tackled"] 
        lower_is_better = ['Fouls']
        radar_position = 'Midfielder'
    if radartype == 'Winger/CAM':
        params = ["npxG", "npxG/Shot", "Fouls Drawn", 'Tackles & Interceptions',
          'Expected Assisted Goals', "Passes into Penalty Area", 'Progressive Carries',
          "Progressive Passes", "Shot Creating Actions", "Shot Distance (Yards)",
          "Shots"]
        lower_is_better = ["Shot Distance (Yards)"]
        radar_position = 'Attacking Midfielder/Winger'
    if radartype == 'Striker':
        params = ["npxG", "Shots", "Shot Distance (Yards)", "Shot Creating Actions",
                  'Expected Assisted Goals', 'Carries into Penalty Area', 
                  'Passes into Penalty Area', 'Aerial Duels Won', 'Fouls Drawn',
                  'Progressive Carries', 'npxG/Shot']
        lower_is_better = ["Shot Distance (Yards)"]
        radar_position = 'Striker'

    return params, lower_is_better, radar_position

def get_percentiles(df, params):
    params = params
    low_vals = []
    high_vals = []
    for p in params:
        vals = df.loc[(df['90s'] >= 20), p].values
        low_perc = float(round(np.percentile(vals, 5),2))
        high_perc = float(round(np.percentile(vals, 95),2))
        low_vals.append(low_perc)
        high_vals.append(high_perc)
    
    return low_vals, high_vals

def get_player_data(df, season, league, team, player):
    player_data = df.loc[(df['season'] == season) &
                     (df['league'] == league) &
                     (df['team'] == team) &
                     (df['player'] == player)]
    
    return player_data

def get_single_player_radar_info(df, league, season):
    player_age = int(df['age'].values[0])
    player_age_str = f'Age: {player_age}'
    game_time = float(df['90s'].values[0])
    appearances = int(df['matches'].values[0])
    league_season_str = f'{league} {season}'
    game_time_appearances_str = f'{game_time} 90s played ({appearances} appearances)'
    
    return player_age_str, league_season_str, game_time_appearances_str

def get_two_player_radar_info(df, name, league, season):
    player_age = int(df['age'].values[0])
    name_age_str = f'{name} ({player_age})'

    game_time = float(df['90s'].values[0])
    appearances = int(df['matches'].values[0])
    league_season_str = f'{league} {season}'
    game_time_appearances_str = f'{game_time} 90s played ({appearances} appearances)'
    
    return name_age_str, league_season_str, game_time_appearances_str

def add_labels_endnote(radar, axs):
    range_labels = radar.draw_range_labels(ax=axs['radar'], fontsize=18, fontproperties = robotto_bold.prop)  # draw the range labels
    param_labels = radar.draw_param_labels(ax=axs['radar'], fontsize=20, offset = 0.5, fontproperties = robotto_bold.prop)  # draw the param labels
    endnote_text = axs['endnote'].text(0.99, 0.55, 'Inspired By: StatsBomb / Rami Moghadam \nData from Fbref', fontsize=15,
                  fontproperties=robotto_bold.prop, ha='right', va='center')
    
def single_player_header(axs, player, team, player_age_str, radar_position, league_season_str, game_time_appearances_str):
    title1_text = axs['title'].text(0.01, 0.55, player, fontsize=28,
                                fontproperties=robotto_bold.prop, ha='left', va='center')
    title2_text = axs['title'].text(0.01, 0.10, team, fontsize=24,
                                    fontproperties=robotto_bold.prop,
                                    ha='left', va='center', color='#B6282F')

    title3_text = axs['title'].text(0.01, -0.31, player_age_str, fontsize=21,
                                    fontproperties=robotto_bold.prop,
                                    ha='left', va='center', color='#B6282F')


    title4_text = axs['title'].text(0.99, 0.55, radar_position, fontsize=28,
                                    fontproperties=robotto_bold.prop, ha='right', va='center')

    title5_text = axs['title'].text(0.99, 0.10, league_season_str, fontsize=24,
                                    fontproperties=robotto_bold.prop,
                                    ha='right', va='center', color='#B6282F')

    title6_text = axs['title'].text(0.99, -0.31, game_time_appearances_str, fontsize=21,
                                    fontproperties=robotto_bold.prop,
                                    ha='right', va='center', color='#B6282F')

def first_player_header(axs, name_age_str, team, league_season_str, game_time_appearances_str):
    title1_text = axs['title'].text(0.01, 0.55, name_age_str, fontsize=28,
                                fontproperties=robotto_bold.prop, ha='left', va='center',
                                color='#B6282F')
    title2_text = axs['title'].text(0.01, 0.10, team, fontsize=24,
                                    fontproperties=robotto_bold.prop,
                                    ha='left', va='center', color='#B6282F')
    title3_text = axs['title'].text(0.01, -0.26, game_time_appearances_str, fontsize=16,
                                    fontproperties=robotto_bold.prop,
                                    ha='left', va='center')
    title3_text = axs['title'].text(0.01, -0.56, league_season_str, fontsize=16,
                                    fontproperties=robotto_bold.prop,
                                    ha='left', va='center')

def second_player_header(axs, name_age_str, team, league_season_str, game_time_appearances_str):
    title1_text = axs['title'].text(0.99, 0.55, name_age_str, fontsize=28,
                                fontproperties=robotto_bold.prop, ha='right', va='center',
                                color='#1f7ced')
    title2_text = axs['title'].text(0.99, 0.10, team, fontsize=24,
                                    fontproperties=robotto_bold.prop,
                                    ha='right', va='center', color='#1f7ced')
    title3_text = axs['title'].text(0.99, -0.26, game_time_appearances_str, fontsize=16,
                                    fontproperties=robotto_bold.prop,
                                    ha='right', va='center')
    title3_text = axs['title'].text(0.99, -0.56, league_season_str, fontsize=16,
                                    fontproperties=robotto_bold.prop,
                                    ha='right', va='center')


def single_player_plot(df, season, league, team, player, radartype):
    
    params, lower_is_better, radar_position = get_params(radartype)
    low_vals, high_vals = get_percentiles(df, params)
    player_data = get_player_data(df, season, league, team, player)

    player_age_str, league_season_str, game_time_appearances_str = get_single_player_radar_info(player_data, league, season)
    player_vals = player_data.loc[:,params].values[0]

    radar = Radar(params, low_vals, high_vals, lower_is_better=lower_is_better,
              round_int=[False]*len(params),
              num_rings= 6,
              ring_width=0.6, center_circle_radius=1)
    fig, axs = grid(figheight=14, grid_height=0.915, title_height=0.06, endnote_height=0.025,
              title_space=0, endnote_space=0, grid_key='radar', axis=False)
    
    radar.setup_axis(ax=axs['radar'])

    rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='#BEC8CE', edgecolor='#B3BCC3')

    radar_output = radar.draw_radar(player_vals, ax=axs['radar'],
                kwargs_radar={'facecolor': '#F75959', 'alpha' : 0.3},
                kwargs_rings={'facecolor': '#F75959', 'alpha' : 0.3}) 
    
    add_labels_endnote(radar, axs)
    single_player_header(axs, player, team, player_age_str, radar_position, league_season_str, game_time_appearances_str)

    return fig

def two_player_plot(df, first_season, first_league, first_team, first_player,
                    second_season, second_league, second_team, second_player, radartype):
    
    params, lower_is_better, radar_position = get_params(radartype)
    low_vals, high_vals = get_percentiles(df, params)
    
    first_player_data = get_player_data(df, first_season, first_league, first_team, first_player)
    second_player_data = get_player_data(df, second_season, second_league, second_team, second_player)

    first_name_age_str, first_league_season_str, first_game_time_appearances_str = get_two_player_radar_info(first_player_data, first_player, first_league, first_season)
    second_name_age_str, second_league_season_str, second_game_time_appearances_str = get_two_player_radar_info(second_player_data, second_player, second_league, second_season)

    first_player_vals = first_player_data.loc[:,params].values[0]
    second_player_vals = second_player_data.loc[:,params].values[0]
    
    radar = Radar(params, low_vals, high_vals, lower_is_better=lower_is_better,
              round_int=[False]*len(params),
              num_rings= 6,
              ring_width=0.6, center_circle_radius=1)
    fig, axs = grid(figheight=14, grid_height=0.915, title_height=0.06, endnote_height=0.025,
              title_space=0, endnote_space=0, grid_key='radar', axis=False)
    
    radar.setup_axis(ax=axs['radar'])

    rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='#BEC8CE', edgecolor='#B3BCC3')

    radar_output = radar.draw_radar_compare(first_player_vals, second_player_vals, ax=axs['radar'],
                        kwargs_radar={'facecolor': '#F75959', 'alpha' : 0.35},
                        kwargs_compare={'facecolor': '#1f7ced', 'alpha': 0.35})
    
    add_labels_endnote(radar, axs)

    first_player_header(axs, first_name_age_str, first_team, first_league_season_str, first_game_time_appearances_str)
    second_player_header(axs, second_name_age_str, second_team, second_league_season_str, second_game_time_appearances_str)
    second_endnote_text = axs['endnote'].text(0.01, 0.55, f'{radar_position} Template', fontsize=15,
                  fontproperties=robotto_bold.prop, ha='left', va='center')
    
    return fig

