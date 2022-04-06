import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, Dash

from mydash.charts_data import VolcanoData
import mydash.create_charts as CC

data = VolcanoData()
data.process_data_for_line_charts()
lc = CC.LineGraph(data)
fig_lc = lc.create_linechart()

data.process_data_for_live_chart()
lb = CC.LiveChart(data)
fig_lb = lb.create_live()


class DashApp2:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/dash_app2/',
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
        self.app.layout = html.Div(children=[
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

    def setup_callbacks(self):
        pass
