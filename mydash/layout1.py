import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, Dash

from mydash.charts_data import VolcanoData
import mydash.create_charts as CC

data = VolcanoData()
data.process_data_for_choropleth()
cc = CC.Choropleth(data)
fig2 = cc.create_choropleth("VOLCANO")
fig3 = cc.create_choropleth("ERUPTIONS")
fig4 = cc.create_choropleth("RATIO")

bc = CC.BarGraph(data)
fig5 = bc.creat_bar_graph("VOLCANO")
fig6 = bc.creat_bar_graph("ERUPTIONS")
fig7 = bc.creat_bar_graph("RATIO")


class DashApp1:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/dash_app1/',
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
        self.app.layout = dbc.Container(fluid=True, children=[
            dbc.Row([
                dbc.Col(width=1),

                dbc.Col(children=[
                    html.Br(),

                    html.H1(children='Volcanoes on the World Map'),

                    html.P(
                        children="The figures for the number of volcanoes and eruptions have been plotted on a world "
                                 "map to "
                                 "visualize the density of volcanoes around the world. The top 10 countries from each "
                                 "category are compared using a bar chart."),
                ]),

                dbc.Col(width=1)
            ]),

            html.Br(),

            dbc.Row(children=[
                dbc.Col(width=1),

                dbc.Col(width=10, children=[
                    dbc.Tabs(children=[
                        dbc.Tab(dbc.Row([
                            dbc.Col(width=4, children=[
                                dcc.Graph(id="volcano-top10", figure=fig5)
                            ]),
                            dbc.Col(width=8, children=[
                                dcc.Graph(id="volcano-choropleth", figure=fig2)
                            ])
                        ]),
                            label="Number Of Volcanoes"
                        ),

                        dbc.Tab(dbc.Row([
                            dbc.Col(width=4, children=[
                                dcc.Graph(id="eruption-top10", figure=fig6)
                            ]),
                            dbc.Col(width=8, children=[
                                dcc.Graph(id="eruption-choropleth", figure=fig3)
                            ])
                        ]),
                            label="Number Of Eruptions", ),

                        dbc.Tab(dbc.Row([
                            dbc.Col(width=4, children=[
                                dcc.Graph(id="ratio-top10", figure=fig7)
                            ]),
                            dbc.Col(width=8, children=[
                                dcc.Graph(id="ratio-choropleth", figure=fig4)
                            ])
                        ]),
                            label="Ratio of Eruptions to Volcanoes", )

                    ])
                ]),

                dbc.Col(width=1)
            ]),
        ])

    def setup_callbacks(self):
        pass
