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
cc = CC.MapBox(data)
fig1 = cc.create_mapbox("Algeria")

layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col(width=1),

        dbc.Col(children=[
            html.Br(),

            html.H1(children='Data for Individual Countries'),

            html.P(
                children="Geographical locations of volcanoes and their number of eruptions is computed for "
                         "individual countries. Please note that, in this Web App , a country and its overseas "
                         "territories are considered as one.")
        ]),

        dbc.Col(width=1)
    ]),

    html.Br(),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(width=3, children=[
            html.H6("Select Country"),
            dcc.Dropdown(data.v_countries,
                         id="country-dropdown",
                         value="Algeria")
        ])
    ]),
    dcc.Graph(id="mapbox",
              figure=fig1)
])


@app.callback(
    Output('mapbox', 'figure'),
    Input('country-dropdown', 'value')
)
def update_mapbox(value):
    fig1 = cc.create_mapbox(value)
    return fig1
