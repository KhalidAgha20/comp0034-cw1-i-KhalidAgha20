import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from mydash.app import app
from mydash.charts_data import VolcanoData
import mydash.create_charts as CC

data = VolcanoData()
data.process_data_for_choropleth()
cc = CC.Choropleth(data)
fig1 = cc.create_choropleth("VOLCANO")
fig2 = cc.create_choropleth("ERUPTIONS")
fig3 = cc.create_choropleth("RATIO")

bc = CC.BarGraph(data)
fig4 = bc.creat_bar_graph("VOLCANO")
fig5 = bc.creat_bar_graph("ERUPTIONS")
fig6 = bc.creat_bar_graph("RATIO")

layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col(width=1),

        dbc.Col(children=[
            html.Br(),

            html.H1(children='Volcanoes on the World Map'),

            html.P(
                children="The figures for the number of volcanoes and eruptions have been plotted on a world map to "
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
                        dcc.Graph(id="volcano-top10", figure=fig4)
                    ]),
                    dbc.Col(width=8, children=[
                        dcc.Graph(id="volcano-choropleth", figure=fig1)
                    ])
                ]),
                    label="Number Of Volcanoes"
                ),

                dbc.Tab(dbc.Row([
                    dbc.Col(width=4, children=[
                        dcc.Graph(id="eruption-top10", figure=fig5)
                    ]),
                    dbc.Col(width=8, children=[
                        dcc.Graph(id="eruption-choropleth", figure=fig2)
                    ])
                ]),
                    label="Number Of Eruptions", ),

                dbc.Tab(dbc.Row([
                    dbc.Col(width=4, children=[
                        dcc.Graph(id="ratio-top10", figure=fig6)
                    ]),
                    dbc.Col(width=8, children=[
                        dcc.Graph(id="ratio-choropleth", figure=fig3)
                    ])
                ]),
                    label="Ratio of Eruptions to Volcanoes", )

            ])
        ]),

        dbc.Col(width=1)
    ]),
])
