import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
from PIL import Image
from pathlib import Path

from flask.helpers import get_root_path

from mydash.charts_data import VolcanoData
from mydash.create_charts import MapBox

data = VolcanoData()
data.process_data_for_choropleth()
cc = MapBox(data)
fig1 = cc.homegraph()

imgpath = Path(__file__).parent.joinpath('assets','logo.png')
PLOTLY_LOGO = Image.open(imgpath)


class DashAppIndex:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/dash_app_index/',
                        suppress_callback_exceptions=True, server=flask_server,
                        external_stylesheets=[dbc.themes.BOOTSTRAP],
                        meta_tags=[{
                            'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'
                        }])

    def setup(self):
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        self.app.layout = dbc.Container([
            html.Div([
                html.Br(),
                html.Img(src=PLOTLY_LOGO, height="200px"),
                html.H1("VOLCANIC ERUPTIONS")
            ], style={'textAlign': 'center'}),
            html.Br(),
            dbc.Row([
                dbc.Col(width=1),
                dbc.Col(width=10, children=[
                    html.H6("Latest Volcanic Eruptions", style={'textAlign': 'center'}),
                    dcc.Graph(id="latest-eruptions",
                              figure=fig1)
                ])
            ])
        ])

    def setup_callbacks(self):
        pass



