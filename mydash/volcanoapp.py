import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from mydash.charts_data import VolcanoData
import mydash.create_charts as CC

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = VolcanoData()

data.process_data_for_line_charts()
lc = CC.LineGraph(data)
fig_lc = lc.create_linechart()

data.process_data_for_choropleth()
cc = CC.Choropleth(data)
datatype = "VOLCANO"
fig_cc = cc.create_choropleth(datatype)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='choropleth',
        figure=fig_cc
    ),

    dcc.Graph(
        id='line-chart',
        figure=fig_lc
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
