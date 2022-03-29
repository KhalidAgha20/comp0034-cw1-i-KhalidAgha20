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
        figure.update_traces(marker_line_width=0)
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
        figure.update_traces(marker_color="#800020")
        figure.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)'
        })
        return figure


class LineGraph:

    def __init__(self, data):
        self.data = data

    def create_linechart(self):
        figure = px.line(self.data.df_year_eruptions,
                         x="YEAR",
                         y="ERUPTIONS",
                         labels={
                             "YEAR": "Year",
                             "ERUPTIONS": "Number of Volcanic Eruptions in the Year",
                         },
                         title="Number of Volcanic Eruptions VS Time Graph"
                         )
        figure.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)'
        },
        )
        return figure


class MapBox:

    def __init__(self, data):
        self.data = data

    def create_mapbox(self, country):
        df = self.data.volcano.loc[self.data.volcano["COUNTRY"] == country]
        px.set_mapbox_access_token(open(".mapbox_token").read())
        fig = px.scatter_mapbox(df,
                                lat="LATITUDE",
                                lon="LONGITUDE",
                                color="ERUPTIONS",
                                color_continuous_scale="bluered",
                                zoom=3.5,
                                hover_name="NAME",
                                labels={
                                    "ERUPTIONS": "Number of Volcanic Eruptions",
                                },
                                )
        fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20)
        )
        return fig

    def homegraph(self):
        df = self.data.eruptions.head(20)
        px.set_mapbox_access_token(open(".mapbox_token").read())
        fig = px.scatter_mapbox(df,
                                lat="Latitude",
                                lon="Longitude",
                                size=df["Number"] * 0 + 1,
                                zoom=1,
                                hover_name="Name"
                                )
        fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20)
        )
        return fig


class LiveChart:

    def __init__(self, data):
        self.data = data

    def create_live(self):
        df = self.data.df_live
        figure = px.bar(df,
                        x="VEI",
                        y="count",
                        animation_frame="Start Year",
                        animation_group="VEI",
                        title="Number of Eruptions for Each VEI"
                        )
        figure.update_traces(width=0.5, marker_color="#800020")
        figure.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            'xaxis': {'title': 'VEI of Eruptions', 'range': [-0.5, 8.5]},
            'yaxis': {'title': 'Number of Eruptions', 'range': [0, 15]}
        })
        return figure


class PolarPlot:

    def __init__(self, data):
        self.data = data

    def create_polar(self, distance):
        df = self.data.df_polar
        figure = px.bar(df,
                        x="COUNTRY",
                        y=distance,
                        labels={
                            "COUNTRY": "Country",
                            distance: "Population in Vicinity of Eruptions",
                        },
                        title='Number of People Living Close to Volcanoes'
                        )
        figure.update_traces(marker_color="#800020")
        figure.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)'
        })
        figure.update_yaxes(type="log")
        return figure
