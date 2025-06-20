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
app.config.suppress_callback_exceptions=True

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

def league_season_dropdowns(num_player):
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
                        clearable = False
                        ), style = {
                            'width' : '230px',})
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
                        value = 'English Premier League',
                        clearable = False
                    ), style = {
                        'width' : '230px'
                    }
                ),
            html.Br(),
            html.Div(id = 'league-inputs')
        ], style = {'marginLeft' : '50px'})
    
@callback(
    dash.dependencies.Output('filtered_df', 'data'),
    dash.dependencies.Output('league-inputs', 'children'),
    dash.dependencies.Input('selectSeason', 'value'),
    dash.dependencies.Input('selectLeague', 'value'),
    
)

def team_dropdown(szn, lg):
    league_season_filtered_df = df[(df['league'] == lg) & (df['season'] == szn)]
    uniqueTeams = league_season_filtered_df['team'].unique()
    
    return (
        league_season_filtered_df.to_dict('records'),
        html.Div([
            html.Label('Select a Team', style = {
                    'fontWeight' : 'bold',
                    'font-size' : '20px' 
                    }),
                html.Div(
                    dcc.Dropdown(
                        id = 'selectTeam',
                        options = uniqueTeams,
                        value = uniqueTeams[0],
                        clearable = False
                    ), style = {
                        'width' : '230px'
                    }
                ),
                html.Div(id = 'team-output')
        ])
    )

@callback(
    dash.dependencies.Output('team-output', 'children'),
    dash.dependencies.Input('selectTeam', 'value'),
    dash.dependencies.Input('filtered_df', 'data')
)

def player_dropdown(team, data):
    df = pd.DataFrame(data)
    player_filtered_df = df[df['team'] == team]
    uniquePlayers = player_filtered_df['player'].unique()
    #print(t)
    return(
        html.Div([
            html.Br(),
            html.Label('Select a Player', style = {
                    'fontWeight' : 'bold',
                    'font-size' : '20px' 
                    }),
                html.Div(
                    dcc.Dropdown(
                        id = 'selectPlayer',
                        options = uniquePlayers,
                        value = uniquePlayers[0],
                        clearable = False
                    ), style = {
                        'width' : '230px'
                    }
                ),
                html.Div(id = 'player_output')
        ])
    )


if __name__ == '__main__':
    app.run(debug =True)