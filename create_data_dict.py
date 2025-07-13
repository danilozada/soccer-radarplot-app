# packages
import pandas as pd
import numpy as np

df = pd.read_csv('radar_data.csv')
df = df.fillna(0)

seasons = df['season'].unique()
league = df['league'].unique()

data_dict = {}

for szn in seasons:
    data_dict[szn] = {}
    for l in league:
        data_dict[szn][l] = {}

for year in data_dict.keys():
    for league in data_dict[year]:
        teams = df[(df['season'] == year) & (df['league'] == league)]['team'].unique()
        for t in teams:
            data_dict[year][league][t] = {}

for year in data_dict.keys():
    for league in data_dict[year].keys():
        for t in data_dict[year][league].keys():
            players = df[(df['season'] == year) & (df['league'] == league) & (df['team'] == t)]['player'].unique()
            data_dict[year][league][t] = list(players)
