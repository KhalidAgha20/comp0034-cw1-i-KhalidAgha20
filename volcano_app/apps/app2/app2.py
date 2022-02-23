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

layout = html.Div(children=[
    html.Br(),

    html.H1(children='Volcano Data on the Map'),

    html.H3(children="T"),

    html.Br(),

    html.H4("Select Chart Type"),
    dcc.Dropdown(id="map-type-dropdown",
                 options=[
                     {'label': 'Number of volcanoes', 'value': 'VOLCANO'},
                     {'label': 'Number of eruptions', 'value': 'ERUPTIONS'},
                     {'label': 'Ratio of eruptions to number of volcanoes', 'value': 'RATIO'},
                 ],
                 value="VOLCANO"),

    dcc.Graph(
        id='yearly-eruptions',
        figure=fig_lc
    )
])

