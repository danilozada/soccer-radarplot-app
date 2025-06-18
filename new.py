import pandas as pd
import numpy as np
import soccerdata as sd
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

uniqueLeagues = ['ENG-Premier League', 'ESP-La Liga', 'FRA-Ligue 1',
       'GER-Bundesliga', 'ITA-Serie A']

def return_standard_dataframe(season):
    standard_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=season, no_cache=True).read_player_season_stats('standard').reset_index()
    return(standard_df)

def return_

global_data = {}

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Radar Plot Generator', style = {'textAlign' : 'center'}),
    html.Div([
        html.Label('Select a Radar Plot', style = {
                'fontWeight' : 'bold',
                'font-size' : '20px' 
                }),
        dcc.RadioItems(['Single Player', 'Player Comparison'], 'Single Player', id = 'plot-type', inline=True)],
        style = {'marginLeft' : '50px'}),
        html.Br(),
        html.Div(id = 'button-select')
])

@callback(
    dash.dependencies.Output('button-select', 'children'),
    dash.dependencies.Input('plot-type', 'value')
)

def create_dropdowns(num_player):
    if num_player == 'Single Player':
        return html.Div([
            html.Div([
                html.Label('Select a Season (ex. 22/23 season; select 2022)', 
                            style = {
                                'font-weight' : 'bold',
                                'font-size' : '20px'            
                    }),
                html.Div(
                    dcc.Dropdown(
                        id = 'selectSeason',
                        options = np.arange(2020, 2025, 1),
                        value = 2024,
                        ), style = {
                            'width' : '30%',})
            ]),
            html.Br(),
            html.Label('Select a league', style = {
                    'fontWeight' : 'bold',
                    'font-size' : '20px' 
                    }),
                html.Div(
                    dcc.Dropdown(
                        id = 'selectLeague',
                        options = uniqueLeagues,
                        value = 'ENG-Premier League'
                    ), style = {
                        'width' : '30%'
                    }
                ),
            html.Br(),
            html.Button('Filter by This Season and League', id = 'szn_league_button', n_clicks = 0),
            html.Div(id = 'league-inputs')
        ], style = {'marginLeft' : '50px'})
    
@callback(
    dash.dependencies.Output('league-inputs', 'children'),
    dash.dependencies.Input('szn_league_button', 'n_clicks'),
    dash.dependencies.State('selectSeason', 'value'),
    dash.dependencies.State('selectLeague', 'value')
)

def season_league_clicker(n_clicks, szn, lg):
    if n_clicks == 0:
        return('Please select a Season and League')
    
    standard_df = return_standard_dataframe(szn)
    global_data['standard_df'] = standard_df

    unique_teams = standard_df[standard_df['league'] == lg]['team'].unique()
    
    return html.Div([
        html.Br(),
        html.Label('Select a team', style = {
                'fontWeight' : 'bold',
                'font-size' : '20px' 
                }),
            html.Div(
                dcc.Dropdown(
                    id = 'selectTeam',
                    options = unique_teams,
                    value = unique_teams[1]
                ), style = {
                    'width' : '30%'
                }
            ),
            html.Br(),
            html.Button('Filter by This Team', id = 'team_button', n_clicks = 0),
            html.Div(id = 'team-output')
    ])

@callback(
    dash.dependencies.Output('team-output', 'children'),
    dash.dependencies.Input('team_button', 'n_clicks'),
    dash.dependencies.State('selectTeam', 'value')
)

def player_clicker(n_clicks, team):
    if n_clicks == 0:
        return('')
    
    standard_df = global_data.get('standard_df', None)

    unique_players = standard_df[standard_df['team'] == team]['player'].unique()

    return html.Div([
        html.Br(),
        html.Label('Select a player', style = {
                'fontWeight' : 'bold',
                'font-size' : '20px' 
                }),
        html.Div(
            dcc.Dropdown(
                id = 'selectPlayer',
                options = unique_players,
                placeholder = ''
            ), style = {
                'width' : '30%'
            }
            ),
        html.Br(),
        html.Label('Select a position', style = {
            'fontWeight' : 'bold',
            'font-size' : '20px' 
                }),
        html.Div(
            dcc.Dropdown(
                id = 'selectPosition',
                options = ['Centerback', 'Fullback', 'Midfielder', 'Winger/CAM', 'Striker'],
                placeholder = ''
            ), style = {
                'width' : '30%'
            }
        ),
        html.Br(),  
        html.Button('Select This Player and Position', id = 'player_button', n_clicks = 0),
        html.Div(id = 'player-output')
    ])




if __name__ == '__main__':
    app.run(debug =True)