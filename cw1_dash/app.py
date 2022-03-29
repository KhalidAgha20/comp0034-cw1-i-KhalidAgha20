from dash import Dash
import dash_bootstrap_components as dbc

css_url = ["https://cdn.jsdelivr.net/npm/foundation-sites@6.7.4/dist/css/foundation.min.css"]

app = Dash(__name__,
           suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"},
           ])

server = app.server


