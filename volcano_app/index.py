from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from pathlib import Path
import base64
from charts_data import VolcanoData
from create_charts import MapBox

from volcano_app.apps.app1 import app1
from volcano_app.apps.app2 import app2
from volcano_app.apps.app3 import app3

from volcano_app.app import app

data = VolcanoData()
data.process_data_for_choropleth()
cc = MapBox(data)
fig1 = cc.homegraph()

PLOTLY_LOGO = 'https://lh4.googleusercontent.com' \
              '/WqiYLPs75TX1SezYdaK7m5FX6hIhgeGA2PbMohIjJmk1ubsm5irk03iSqKM2LPEasC7wkjJ9RLJ1xQ=w3840-h1933 '

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("VOLCANIC ERUPTION STATISTICS", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"}
            ),
            dbc.NavItem(dbc.NavLink("Volcanoes on the World Map", href="/app1/"), className="text-danger", ),
            dbc.NavItem(dbc.NavLink("Yearly Data", href="/app2/"), id="page-2-link"),
            dbc.NavItem(dbc.NavLink("Search By Country", href="/app3/"), id="page-3-link")
        ]
    ),
    color="#800020",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

index_layout = dbc.Container([
    html.Div([
        html.Br(),
        html.Img(src=PLOTLY_LOGO, height="300px"),
        html.H1("VOLCANIC ERUPTION STATISTICS")
    ], style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(width=6, children=[
            html.H6("Latest Volcanic Eruptions", style={'textAlign': 'center'}),
            dcc.Graph(id="latest-eruptions",
                      figure=fig1)
        ])
    ])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app1/':
        return app1.layout
    if pathname == '/app2/':
        return app2.layout
    if pathname == '/app3/':
        return app3.layout
    elif pathname == '/':
        return index_layout
    else:
        return '404 Page Not Found'


if __name__ == '__main__':
    app.run_server(debug=True, port=5050)
