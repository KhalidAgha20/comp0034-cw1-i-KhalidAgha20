import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output

from cw1_dash.app import app
from cw1_dash.charts_data import VolcanoData
import cw1_dash.create_charts as CC

data = VolcanoData()
data.process_data_for_circular_bar()

pp = CC.PolarPlot(data)
fig1 = pp.create_polar('POP_5')

layout = html.Div(children=[
    html.Br(),
    dbc.Row([
        dbc.Col(width=1),

        dbc.Col(width=10, children=[
            html.H1(children='Population Near Volcanoes'),
        ]),

        dbc.Col(width=1)
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(width=1),

        dbc.Col(width=9, children=[
            dcc.Graph(
                id='polar-plot',
                figure=fig1,
            )
        ]),

        dbc.Col(width=1)
    ]),

    dbc.Row([
        dbc.Col(width=3),
        dbc.Col(width=6, children=[
            dcc.Slider(5,
                       100,
                       step=None,
                       marks={5: '5',
                              10: '10',
                              30: '30',
                              100: '100'
                              },
                       id='slider'
                       ),
            html.P('Distance from the Volcano (km)', style={'textAlign': 'center'})
        ]),
        dbc.Col(width=3)
    ])

])


@app.callback(
    Output('polar-plot', 'figure'),
    Input('slider', 'value')
)
def update_polar(value):
    fig1 = pp.create_polar('POP_{}'.format(value))
    return fig1