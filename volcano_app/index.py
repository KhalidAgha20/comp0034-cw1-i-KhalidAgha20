from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from pathlib import Path
import base64

from volcano_app.apps.app1 import app1
from volcano_app.apps.app2 import app2


from volcano_app.app import app

PLOTLY_LOGO = 'https://lh5.googleusercontent.com/FNOPNon6IvWz9qC7Pp04q-qhEnCq9Li9es9tpQcNfSyio2RIFcOgH_5' \
              '-zFoVdADmGsJv86_4IP1RQ7t1gCoP=w3840-h1933 '

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
                style={"textDecoration": "none"},
            ),
            dbc.NavItem(dbc.NavLink("Volcanoes on the World Map", href="/app1/"), className="text-danger",),
            dbc.NavItem(dbc.NavLink("Yearly Data", href="/app2/"), id="page-2-link"),
            dbc.NavItem(dbc.NavLink("By Country", href="/app2/"), id="page-3-link")
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

index_layout = html.Div([
    html.P('Hello')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app1/':
        return app1.layout
    if pathname == '/app2/':
        return app2.layout
    elif pathname == '/':
        return index_layout
    else:
        return '404 Page Not Found'


if __name__ == '__main__':
    app.run_server(debug=True, port=5050)