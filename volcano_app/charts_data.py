from pathlib import Path
import pandas as pd


class VolcanoData:
    def __init__(self):
        self.volcano = pd.DataFrame()
        self.eruptions = pd.DataFrame()
        self.frame = pd.DataFrame()
        self.import_data()
        self.countries = []

    def import_data(self):
        volcano_csv = Path(__file__).parent.joinpath('data', 'volcano_list.csv')
        eruptions_csv = Path(__file__).parent.joinpath('data', 'eruptions_list.csv')
        self.volcano = pd.read_csv(volcano_csv)
        self.eruptions = pd.read_csv(eruptions_csv)

    def process_data_for_choropleth(self):
        self.countries = self.volcano['COUNTRY'].unique().tolist()
        self.countries.sort()
        volcano_numbers = self.volcano['COUNTRY'].value_counts()[self.countries]
        self.frame = pd.DataFrame(list(zip(self.countries, volcano_numbers)), columns= ["COUNTRY", "VOLCANO"])

        eruption_countries = self.eruptions['Country'].unique().tolist()
        eruption_numbers = self.eruptions['Country'].value_counts()[eruption_countries]
        eruptions = pd.DataFrame(list(zip(eruption_countries, eruption_numbers)), columns= ["Country", "ERUPTIONS"])

        self.frame = self.frame.merge(eruptions, how="left", left_on="COUNTRY", right_on="Country")
        self.frame.drop(["Country"], axis = 1, inplace = True)
        self.frame['ERUPTIONS'] = self.frame['ERUPTIONS'].fillna(0)







x = VolcanoData()
x.process_data_for_choropleth()
x.show_data()
