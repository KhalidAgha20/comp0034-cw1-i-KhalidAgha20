import plotly.graph_objs as go
import plotly.express as px
import numpy as np


class Choropleth:

    def __init__(self, data):
        self.data = data

    def create_choropleth(self, data_type):
        figure = px.choropleth(self.data.df_choropleth,
                               locationmode="country names",
                               locations="COUNTRY",
                               color=data_type,
                               hover_name="COUNTRY",
                               )
        return figure


class LineGraph:

    def __init__(self, data):
        self.data = data

    def create_linechart(self):
        figure = px.line(self.data.df_year_eruptions,
                         x="YEAR",
                         y="ERUPTIONS"
                         )
        return figure
