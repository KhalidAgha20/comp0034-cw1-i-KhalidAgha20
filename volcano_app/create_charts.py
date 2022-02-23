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
                               color=np.log10(self.data.df_choropleth[data_type] + 1),
                               hover_name="COUNTRY",
                               hover_data=["VOLCANO", "ERUPTIONS", "RATIO"],
                               color_continuous_scale="Reds",
                               labels=({"VOLCANO": "Number of Volcanoes",
                                        "ERUPTIONS": "Number of Eruptions",
                                        "RATIO": "Ratio of Eruptions to Volcanoes"
                                        })
                               )
        return figure


class BarGraph:

    def __init__(self, data):
        self.data = data

    def creat_bar_graph(self, column):
        figure = px.bar(self.data.df_choropleth.sort_values(column, ascending=False).head(10),
                        y="COUNTRY",
                        x=column,
                        orientation="h",
                        title="Top 10 Countries",
                        labels={"COUNTRY": ""}
                        )
        figure.update_traces(marker_color='red')
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
