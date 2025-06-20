import pandas as pd
import numpy as np
import soccerdata as sd
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

df = pd.read_csv('radar_data.csv')

uniqueLeagues = df['league'].unique()

def return_standard_dataframe(season):
    standard_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=season, no_cache=True).read_player_season_stats('standard').reset_index()
    return(standard_df)


app = Dash(__name__)


app.layout = html.Div([
    html.Div([
        html.H1('Radar Plot Generator', style = {'textAlign' : 'center'}),
        html.Div([
            html.Label('Select a Season (for 2022-2023 season; select 2022)', 
                        style = {
                            'font-weight' : 'bold',
                            'font-size' : '20px'            
                }),
            html.Div(
                dcc.Dropdown(
                    id = 'selectSeason',
                    options = np.arange(2020, 2025, 1),
                    value = '',
                    placeholder = '',
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
                    placeholder = ''
                ), style = {
                    'width' : '30%'
                }
            )
    ]),
    html.Br(),
    html.Button('Filter by This Season and League', id = 'szn_league_button', n_clicks = 0),
    html.Div(id = 'league-inputs')
], style = {'marginLeft' : '150px'})
    
@callback(
    dash.dependencies.Output('league-inputs', 'children'),
    dash.dependencies.Input('szn_league_button', 'n_clicks'),
    dash.dependencies.State('selectSeason', 'value'),
    dash.dependencies.State('selectLeague', 'value')
)

def season_league_clicker(n_clicks, szn, lg):
    if n_clicks == 0:
        return('Please select a Season and League')
    