import pandas as pd
import numpy as np
import soccerdata as sd
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

df = pd.read_csv('radar_data.csv')

uniqueLeagues = df['league'].unique()
uniqueSeasons = df['season'].unique()

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Radar Plot Generator', style = {'textAlign' : 'center'}),

    dcc.Store(id = 'filtered_df'),

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
                html.Label('Select a Season', 
                            style = {
                                'font-weight' : 'bold',
                                'font-size' : '20px'            
                    }),
                html.Div(
                    dcc.Dropdown(
                        id = 'selectSeason',
                        options = uniqueSeasons,
                        value = '2024/2025',
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
                        value = 'English Premier League'
                    ), style = {
                        'width' : '30%'
                    }
                ),
            html.Br(),
            html.Button('Filter by This Season and League', id = 'szn_league_button', n_clicks = 0),
            html.Div(id = 'league-inputs')
        ], style = {'marginLeft' : '50px'})
    
@callback(
    dash.dependencies.Output('filtered_df', 'data'),
    dash.dependencies.Output('league-inputs', 'children'),
    dash.dependencies.Input('szn_league_button', 'n_clicks'),
    dash.dependencies.State('selectSeason', 'value'),
    dash.dependencies.State('selectLeague', 'value')
)

def season_league_clicker(n_clicks, szn, lg):
    if n_clicks == 0:
        return dash.no_update, 'Please select a Season and League'

    league_season_filtered_df = df[(df['league'] == lg) & (df['season'] == szn)]
    uniqueTeams = league_season_filtered_df['team'].unique()
    
    return (
        league_season_filtered_df.to_dict('records'),
        html.Div([
            html.Br(),
            html.Label('Select a team', style = {
                    'fontWeight' : 'bold',
                    'font-size' : '20px' 
                    }),
                html.Div(
                    dcc.Dropdown(
                        id = 'selectTeam',
                        options = uniqueTeams,
                        value = uniqueTeams[1]
                    ), style = {
                        'width' : '30%'
                    }
                ),
                html.Br(),
                html.Button('Filter by This Team', id = 'team_button', n_clicks = 0),
                html.Div(id = 'team-output')
        ])
    )

@callback(
    dash.dependencies.Output('team-output', 'children'),
    dash.dependencies.Input('team_button', 'n_clicks'),
    dash.dependencies.State('filtered_df', 'data'),
    dash.dependencies.State('selectTeam', 'value')
)

def player_clicker(n_clicks, data, team):
    if n_clicks == 0:
        return('')

    df = pd.DataFrame(data)
    uniquePlayers = df[df['team'] == team]['player'].unique()

    return html.Div([
        html.Br(),
        html.Label('Select a player', style = {
                'fontWeight' : 'bold',
                'font-size' : '20px' 
                }),
        html.Div(
            dcc.Dropdown(
                id = 'selectPlayer',
                options = uniquePlayers,
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