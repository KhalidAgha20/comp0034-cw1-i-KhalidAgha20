import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output

from volcano_app.app import app
from volcano_app.charts_data import VolcanoData
import volcano_app.create_charts as CC

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
