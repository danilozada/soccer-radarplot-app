import pandas as pd
import numpy as np
import soccerdata as sd
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash()

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app.layout = html.Div([
    html.H1('Radar Plot Generator', style = {'textAlign' : 'center'}),
    html.Div([
        html.Label('Select a Radar Plot', style = {
                'fontWeight' : 'bold',
                'font-size' : '20px' 
                }),
        dcc.RadioItems(['Single Player', 'Player Comparison'], 'Single Player', id = 'plot-type', inline=True)],
        style = {'marginLeft' : '150px'}),
        html.Div(id = 'button-select')
])

@callback(
    dash.dependencies.Output('button-select', 'children'),
    dash.dependencies.Input('plot-type', 'value')
)

def func(t):
    if t == 'Single Player':
        return html.Div(className = 'row', children = [
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
        html.Div([
            html.Label('Select a league', style = {
                    'fontWeight' : 'bold',
                    'font-size' : '20px' 
                    }),
            html.Div(
                dcc.Dropdown(
                    id = 'selectLeague',
                    options = ['yes', 'no'],
                    placeholder = ''
                ), style = {
                    'width' : '30%'
                }
            )
        ])], style = {'display' : 'flex'})


if __name__ == '__main__':
    app.run(debug =True)
    