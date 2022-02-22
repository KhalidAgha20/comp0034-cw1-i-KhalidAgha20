import plotly.graph_objs as go
import plotly.express as px


class Choropleth:

    def __init__(self, data):
        self.data = data

    def create_choropleth(self, data_type):
        figure = px.choropleth(self.data.df_choropleth,
                               locations="ISO3",
                               color=data_type,
                               hover_name="COUNTRY",
                               )
        print(self.data.df_choropleth)
        return figure
