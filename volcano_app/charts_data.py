from pathlib import Path
import pandas as pd


class VolcanoData:
    def __init__(self):
        self.volcano = pd.DataFrame()
        self.eruptions = pd.DataFrame()
        self.iso = pd.DataFrame()
        self.df_choropleth = pd.DataFrame()
        self.df_year_eruptions = pd.DataFrame()
        self.countries = []
        self.import_data()


    def import_data(self):
        volcano_csv = Path(__file__).parent.joinpath('data', 'volcano_list.csv')
        eruptions_csv = Path(__file__).parent.joinpath('data', 'eruptions_list.csv')
        iso_csv = Path(__file__).parent.joinpath('data', 'iso.csv')
        self.volcano = pd.read_csv(volcano_csv)
        self.eruptions = pd.read_csv(eruptions_csv)
        self.iso = pd.read_csv(iso_csv)
        self.countries = self.eruptions['Country'].unique().tolist()
        self.countries.sort()

    def process_data_for_choropleth(self):
        countries = self.volcano['COUNTRY'].unique().tolist()
        countries.sort()
        volcano_numbers = self.volcano['COUNTRY'].value_counts()[countries]
        self.df_choropleth = pd.DataFrame(list(zip(countries, volcano_numbers)), columns= ["COUNTRY", "VOLCANO"])

        eruption_numbers = self.eruptions['Country'].value_counts()[self.countries]
        eruptions = pd.DataFrame(list(zip(self.countries, eruption_numbers)), columns= ["Country", "ERUPTIONS"])

        self.df_choropleth = self.df_choropleth.merge(eruptions, how="left", left_on="COUNTRY", right_on="Country")
        self.df_choropleth.drop(["Country"], axis = 1, inplace = True)
        self.df_choropleth['ERUPTIONS'] = self.df_choropleth['ERUPTIONS'].fillna(0)
        self.df_choropleth["RATIO"]= self.df_choropleth["ERUPTIONS"]/self.df_choropleth["VOLCANO"]
        self.df_choropleth=self.df_choropleth.merge(self.iso, how="left", left_on="COUNTRY", right_on="Country")
        self.df_choropleth.drop(["Country"], axis=1, inplace=True)

    def process_data_for_line_charts(self):
        years = self.eruptions["Start Year"].unique().tolist()
        years.sort()
        eruptions_per_year = self.eruptions["Start Year"].value_counts()[years]
        self.df_year_eruptions = pd.DataFrame(list(zip(years, eruptions_per_year)), columns=["YEAR", "ERUPTIONS"])
