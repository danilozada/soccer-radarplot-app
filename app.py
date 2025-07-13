import io
import base64
import pandas as pd
import numpy as np
import soccerdata as sd
import dash
import plotly
from dash import Dash, html, dcc, callback, Output, Input, ALL, State, MATCH, ctx
import plotly.express as px
from radar_function import single_player_plot, two_player_plot
import matplotlib
matplotlib.use('Agg')
from create_data_dict import df, data_dict

data_dict = data_dict
df = df
radar_types = ['Centerback', 'Fullback', 'Midfielder', 'Winger/CAM', 'Striker']
label_style = {
                'fontWeight' : 'bold',
                'fontSize' : '20px'
}

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1('Radar Plot Generator', style = {'textAlign' : 'center'}),
    html.Div([
            html.Div([
            html.Label('Select Number of Players',
                style = label_style),
            html.Br(),
            dcc.RadioItems(
                options = ['Single Player', 'Two Players'], 
                value = 'Single Player', 
                id = 'player-num-select', 
                inline=True
            ),
            html.Div(id = 'player-response'),
            ],
            style = {
                'marginLeft' : '10%'
            }),
        html.Div(id = 'final-output')
    ], 
    style={'display': 'flex', 
              'flexDirection': 'row',
              'justifyContent' : 'space-between'
    })
])

@callback(
    Output('player-response', 'children'),
    Input('player-num-select', 'value')
)

def choosing_dropdown(val):
    if val == 'Single Player':
        return single_player_dropdowns()
    if val == 'Two Players':
        return two_player_dropdowns()
    
def single_player_dropdowns():
    return html.Div([
            html.Br(),
            html.Label('Select a Season',
                style = label_style),
            html.Div(
                dcc.Dropdown(
                    id = {'type' : 'dropdown', 'index' : 'select-season'},
                    options = [{'label': k, 'value': k} for k in data_dict.keys()],
                    value = '2024/2025',
                    clearable = False,
                ), 
                style = {'width' : '230px'}
            ),
            html.Br(),
            html.Label('Select a League',
                       style = label_style),
            html.Div(
                dcc.Dropdown(
                    id = {'type' : 'dropdown', 'index' : 'select-league'},
                    options = [{'label': k, 'value': k} for k in data_dict['2024/2025'].keys()],
                    value = 'English Premier League',
                    clearable = False,
                ),
                style = {'width' : '230px'}
            ),
            html.Br(),
            html.Label('Select a Team',
                       style = label_style),
            html.Div(
                dcc.Dropdown(
                    id = {'type' : 'team_drop', 'index' : 'select-team'},
                    clearable = False),
                style = {'width' : '230px'}
            ),
            html.Br(),
            html.Label('Select a Player',
                       style = label_style),
            html.Div(
                dcc.Dropdown(
                    id = {'type' : 'player_drop', 'index' : 'select-player'},
                    clearable = False),
                style = {'width' : '230px'}
            ),
            html.Br(),
            html.Label('Select a Radar Type', style =
                    label_style),
                html.Div(
                    dcc.Dropdown(
                        id = 'select-radar-type',
                        options = radar_types,
                        value = radar_types[0],
                        clearable = False
                    ), style = {
                        'width' : '230px'
                    }
                ),
            html.Br(),
            html.Button('Create radar plot', id = 'single-radar-button', n_clicks = 0),
            html.Div(id = 'initial-inputs-single')
        ])

def two_player_dropdowns():
    return html.Div([
            html.Div([
                html.Br(),
                html.Label('First Player Season',
                    style = label_style),
                html.Div(
                    dcc.Dropdown(
                        id = {'type' : 'first-player-compare', 'index' : 'first-season'},
                        options = [{'label': k, 'value': k} for k in data_dict.keys()],
                        value = '2024/2025',
                        clearable = False,
                    ), 
                    style = {'width' : '230px',
                             'marginRight' : '20px'}
                ),
                html.Br(),
                html.Label('First Player League',
                        style = label_style),
                html.Div(
                    dcc.Dropdown(
                        id = {'type' : 'first-player-compare', 'index' : 'first-league'},
                        options = [{'label': k, 'value': k} for k in data_dict['2024/2025'].keys()],
                        value = 'English Premier League',
                        clearable = False,
                    ),
                    style = {'width' : '230px'}
                ),
                html.Br(),
                html.Label('Select First Team',
                        style = label_style),
                html.Div(
                    dcc.Dropdown(
                        id = {'type' : 'first-team-drop', 'index' : 'first-team'},
                        clearable = False),
                    style = {'width' : '230px'}
                ),
                html.Br(),
                html.Label('Select First Player',
                        style = label_style),
                html.Div(
                    dcc.Dropdown(
                        id = {'type' : 'first-player-drop', 'index' : 'first-player'},
                        clearable = False),
                    style = {'width' : '230px'}
                ),
                html.Br(),
                html.Label('Select a Radar Type', style =
                        label_style),
                    html.Div(
                        dcc.Dropdown(
                            id = 'select-two-player-radar',
                            options = radar_types,
                            value = radar_types[0],
                            clearable = False
                        ), 
                        style = {
                            'width' : '230px'
                        }
                    ),
                html.Br(),
                html.Button('Create radar plot', id = 'multiple-radar-button', n_clicks = 0),
                html.Div(id = 'initial-inputs-double')
            ]),
            html.Div([
                html.Div([
                    html.Br(),
                    html.Label('Second Player Season',
                        style = label_style),
                    html.Div(
                        dcc.Dropdown(
                            id = {'type' : 'second-player-compare', 'index' : 'second-season'},
                            options = [{'label': k, 'value': k} for k in data_dict.keys()],
                            value = '2024/2025',
                            clearable = False,
                        ), 
                        style = {'width' : '230px'}
                    ),
                    html.Br(),
                    html.Label('Second Player League',
                            style = label_style),
                    html.Div(
                        dcc.Dropdown(
                            id = {'type' : 'second-player-compare', 'index' : 'second-league'},
                            options = [{'label': k, 'value': k} for k in data_dict['2024/2025'].keys()],
                            value = 'English Premier League',
                            clearable = False,
                        ),
                        style = {'width' : '230px'}
                    ),
                    html.Br(),
                    html.Label('Select Second Team',
                            style = label_style),
                    html.Div(
                        dcc.Dropdown(
                            id = {'type' : 'second-team-drop', 'index' : 'second-team'},
                            clearable = False),
                        style = {'width' : '230px'}
                    ),
                    html.Br(),
                    html.Label('Select First Player',
                            style = label_style),
                    html.Div(
                        dcc.Dropdown(
                            id = {'type' : 'second-player-drop', 'index' : 'second-player'},
                            clearable = False),
                        style = {'width' : '230px'}
                    )   
                ])
            ]),
            html.Div(id = 'second-inputs')], style = {'display' :'flex'})

@callback(
    Output({'type' : 'team_drop', 'index' : 'select-team'}, 'options'),
    Output({'type' : 'team_drop', 'index' : 'select-team'}, 'value'),
    Input({'type' : 'dropdown', 'index': ALL}, 'value')
)

def set_team_options(initial_vals):
    teams = data_dict[initial_vals[0]][initial_vals[1]].keys()
    team_options = [{'label': i, 'value': i} for i in  teams]
    team_select = list(teams)[0]
    return team_options, team_select

@callback(
    Output({'type' : 'player_drop', 'index' : 'select-player'}, 'options'),
    Output({'type' : 'player_drop', 'index' : 'select-player'}, 'value'),
    Input({'type' : 'dropdown', 'index': ALL}, 'value'),
    Input({'type' : 'team_drop', 'index': ALL}, 'value'),
)
    
def set_player_options(seasonleague, team):
    season = seasonleague[0]
    league = seasonleague[1]
    team = team[0]
    players = data_dict[season][league][team]
    player_options = [{'label': i, 'value': i} for i in  players]
    player_select = players[0]
    return player_options, player_select

@callback(
    Output({'type' : 'first-team-drop', 'index' : 'first-team'}, 'options'),
    Output({'type' : 'first-team-drop', 'index' : 'first-team'}, 'value'),
    Input({'type' : 'first-player-compare', 'index': ALL}, 'value'),
)

def set_first_team_options(first_player_vals):
    first_season = first_player_vals[0]
    first_league = first_player_vals[1]
    teams = data_dict[first_season][first_league].keys()
    team_options = [{'label': i, 'value': i} for i in  teams]
    team_select = list(teams)[0]
    return team_options, team_select

@callback(
    Output({'type' : 'second-team-drop', 'index' : 'second-team'}, 'options'),
    Output({'type' : 'second-team-drop', 'index' : 'second-team'}, 'value'),
    Input({'type' : 'second-player-compare', 'index': ALL}, 'value'),
)

def set_second_team_options(second_player_vals):
    second_season = second_player_vals[0]
    second_league = second_player_vals[1]
    teams = data_dict[second_season][second_league].keys()
    team_options = [{'label': i, 'value': i} for i in  teams]
    team_select = list(teams)[0]
    return team_options, team_select

@callback(
    Output({'type' : 'first-player-drop', 'index' : 'first-player'}, 'options'),
    Output({'type' : 'first-player-drop', 'index' : 'first-player'}, 'value'),
    Input({'type' : 'first-player-compare', 'index': ALL}, 'value'),
    Input({'type' : 'first-team-drop', 'index': ALL}, 'value'),
)

def set_first_player_options(seasonleague, team):
    season = seasonleague[0]
    league = seasonleague[1]
    team = team[0]
    players = data_dict[season][league][team]
    player_options = [{'label': i, 'value': i} for i in  players]
    player_select = players[0]
    return player_options, player_select

@callback(
    Output({'type' : 'second-player-drop', 'index' : 'second-player'}, 'options'),
    Output({'type' : 'second-player-drop', 'index' : 'second-player'}, 'value'),
    Input({'type' : 'second-player-compare', 'index': ALL}, 'value'),
    Input({'type' : 'second-team-drop', 'index': ALL}, 'value'),
)

def set_second_player_options(seasonleague, team):
    season = seasonleague[0]
    league = seasonleague[1]
    team = team[0]
    players = data_dict[season][league][team]
    player_options = [{'label': i, 'value': i} for i in  players]
    player_select = players[0]
    return player_options, player_select

@callback(
    Output('final-output', 'children', allow_duplicate = True),
    Output('final-output', 'style', allow_duplicate = True),
    Input('single-radar-button', 'n_clicks'),
    State({'type' : 'dropdown', 'index': ALL}, 'value'),
    State({'type' : 'team_drop', 'index' : 'select-team'}, 'value'),
    State({'type' : 'player_drop', 'index' : 'select-player'}, 'value'),
    State('select-radar-type', 'value'),
    prevent_initial_call=True
)

def create_single_player_radar_plot(n_clicks, seasonleague, team, player, radartype):
    if not n_clicks:
        return dash.no_update
    
    single_style = {'width' : '55%',
                        'marginRight' : '25%'}
    
    season = seasonleague[0]
    league = seasonleague[1]
    
    fig = single_player_plot(df, season, league, team, player, radartype)
    img_bytes = io.BytesIO()
    fig.savefig(img_bytes, format = 'png')
    img_bytes.seek(0)
    encoded = base64.b64encode(img_bytes.read()).decode()

    return html.Div([
        html.Img(src = 'data:image/png;base64,{}'.format(encoded),
                    style = {'width' : '70%'})],
        #html.Div([dcc.Dropdown(id = 'yes')]),
        style = {'display' :'flex', 'justifyContent': 'center',
                 'alignItems' : 'flex-start'
        }), single_style

@callback(
    Output('final-output', 'children', allow_duplicate = True),
    Output('final-output', 'style', allow_duplicate = True),
    Input('multiple-radar-button', 'n_clicks'),
    State({'type' : 'first-player-compare', 'index' : ALL}, 'value'),
    State({'type' : 'first-team-drop', 'index' : 'first-team'}, 'value'),
    State({'type' : 'first-player-drop', 'index' : 'first-player'}, 'value'),
    State({'type' : 'second-player-compare', 'index' : ALL}, 'value'),
    State({'type' : 'second-team-drop', 'index' : 'second-team'}, 'value'),
    State({'type' : 'second-player-drop', 'index' : 'second-player'}, 'value'),
    State('select-two-player-radar', 'value'),
    prevent_initial_call=True
)

def create_two_player_radar_plot(n_clicks, first_seasonleague, first_team, first_player, second_seasonleague, second_team, second_player, radartype):
    if not n_clicks:
        return dash.no_update
    
    double_style = {'width' : '65%',
                        'marginRight' : '12%'}
    
    first_season = first_seasonleague[0]
    first_league = first_seasonleague[1]

    second_season = second_seasonleague[0]
    second_league = second_seasonleague[1]
    
    fig = two_player_plot(df, first_season, first_league, first_team, first_player, second_season, second_league, second_team, second_player, radartype)
    img_bytes = io.BytesIO()
    fig.savefig(img_bytes, format = 'png')
    img_bytes.seek(0)
    encoded = base64.b64encode(img_bytes.read()).decode()

    return html.Div([
        html.Img(src = 'data:image/png;base64,{}'.format(encoded),
                    style = {'width' : '70%'})],
        #html.Div([dcc.Dropdown(id = 'yes')]),
        style = {'display' :'flex', 'justifyContent': 'center',
                 'alignItems' : 'flex-start'
        }), double_style

@callback(
    Output('final-output', 'children', allow_duplicate=True),
    Input('player-num-select', 'value'),
    prevent_initial_call = True
)

def clear_graph(mode):
    return None

if __name__ == '__main__':
    app.run(debug =True)