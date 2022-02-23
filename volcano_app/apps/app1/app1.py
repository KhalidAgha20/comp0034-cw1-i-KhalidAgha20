import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output

from volcano_app.app import app
from volcano_app.charts_data import VolcanoData
import volcano_app.create_charts as CC

data = VolcanoData()
data.process_data_for_choropleth()
cc = CC.Choropleth(data)
fig_cc = cc.create_choropleth("VOLCANO")
fig2 = cc.create_choropleth("VOLCANO")
fig3 = cc.create_choropleth("RATIO")

layout = html.Div(children=[
    html.Br(),

    html.H1(children='Volcano Data on the Map'),

    html.P(children="Choose one bitcvh"),

    html.Br(),


    dbc.Tabs(className="nav nav-pills", children=[
        dbc.Tab(dcc.Graph(id="volcano-choropleth", figure=fig_cc), label="Recycling by area"),
        dbc.Tab(dcc.Graph(id="eruption-choropleth", figure=fig2), label="Recycling by year"),
        dbc.Tab(dcc.Graph(id="ratio-choropleth", figure=fig3), label="Recycling by year")
    ])
])

