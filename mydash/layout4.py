import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, Dash

from mydash.app import app
from mydash.charts_data import VolcanoData
import mydash.create_charts as CC

data = VolcanoData()
data.process_data_for_circular_bar()

pp = CC.PolarPlot(data)
fig9 = pp.create_polar('POP_5')


class DashApp4:
    def __init__(self, flask_server):
        self.app = Dash(name=self.__class__.__name__, routes_pathname_prefix='/dash_app4/',
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
                    html.H1(children='Population Near Volcanoes'),
                ]),

                dbc.Col(width=1)
            ]),

            html.Br(),

            dbc.Row([
                dbc.Col(width=1),

                dbc.Col(width=9, children=[
                    dcc.Graph(
                        id='polar-plot',
                        figure=fig9,
                    )
                ]),

                dbc.Col(width=1)
            ]),

            dbc.Row([
                dbc.Col(width=3),
                dbc.Col(width=6, children=[
                    dcc.Slider(5,
                               100,
                               step=None,
                               marks={5: '5',
                                      10: '10',
                                      30: '30',
                                      100: '100'
                                      },
                               id='slider'
                               ),
                    html.P('Distance from the Volcano (km)', style={'textAlign': 'center'})
                ]),
                dbc.Col(width=3)
            ])

        ])

    def setup_callbacks(self):
        @self.app.callback(
            Output('polar-plot', 'figure'),
            Input('slider', 'value')
        )
        def update_polar(value):
            fig9 = pp.create_polar(f'POP_{value}')
            return fig9
