html.Div([
        html.Label('Select a League', style = {
            'font-weight' : 'bold'
            }),
            html.Div(
                dcc.Dropdown(
                    id = 'league',
                    options = ['EPL', 'La Liga'],
                    value = 'str',
                    placeholder = ''
                ), style = {
                    'width' : '30%',
                    'padding' : 20})
        ])
    ], style = {'display' : 'flex', 'flexDirection' : 'row'}