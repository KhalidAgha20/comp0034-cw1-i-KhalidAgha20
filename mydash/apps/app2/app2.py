import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output

from mydash.app import app
from mydash.charts_data import VolcanoData
import mydash.create_charts as CC

data = VolcanoData()
data.process_data_for_line_charts()
lc = CC.LineGraph(data)
fig_lc = lc.create_linechart()

data.process_data_for_live_chart()
lb = CC.LiveChart(data)
fig_lb = lb.create_live()

layout = html.Div(children=[
    html.Br(),
    dbc.Row([
        dbc.Col(width=1),

        dbc.Col(width=10, children=[
            html.H1(children='Change in Number of Volcano Eruptions'),
        ]),

        dbc.Col(width=1)
    ]),

    dbc.Row([
        dbc.Col(width=1),

        dbc.Col(width=10, children=[
            dcc.Graph(
                id='yearly-eruptions',
                figure=fig_lc,
            )
        ]),

        dbc.Col(width=1)
    ]),

    dbc.Row([
        dbc.Col(width=1),

        dbc.Col(width=10, children=[
            dcc.Graph(
                id='live-chart',
                figure=fig_lb,
            )
        ]),

        dbc.Col(width=1)
    ]),
])
