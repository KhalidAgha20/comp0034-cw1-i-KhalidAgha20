import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from volcano_app.charts_data import VolcanoData
from volcano_app.create_charts import Choropleth

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = VolcanoData()
data.process_data_for_choropleth()

cc=Choropleth(data)
data_type = "ERUPTIONS"
fig_cc = cc.create_choropleth(data_type)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig_cc
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
