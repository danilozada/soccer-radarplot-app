import pandas as pd
import numpy as np
import soccerdata as sd
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

standard_df = sd.FBref(leagues="Big 5 European Leagues Combined", seasons=2024, no_cache=True).read_player_season_stats('standard').reset_index()
uniqueLeagues = standard_df['league'].unique()


app = Dash(__name__)


app.layout = html.Div([
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
                value = 2024,
                placeholder = '',
                ), style = {
                    'width' : '30%',})
    ], style = {'marginLeft' : '150px'}),
    html.Div(id = 'seasonOutput')
])
    
@callback(
    dash.dependencies.Output('seasonOutput', 'children'),
    dash.dependencies.Input('selectSeason', 'value')
)
def update_output_div(input_value):

    

    return html.Div([
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
            
    ], style = {'marginLeft' : '150px'})

if __name__ == '__main__':
    app.run(debug =True)