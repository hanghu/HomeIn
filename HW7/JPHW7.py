## Folium mapping

'''Populating the map with clusters of houses and a heat map of crime rates.'''

#import system modules
import os

#import data manipulators
import pandas as pd

#import folium plugins
from folium.plugins import MarkerCluster
import folium
from folium import plugins

#load King County datasets
crimes = pd.read_csv('King_County_Sheriff_s_Office.csv')
houses = pd.read_csv("kc_house_data.csv", parse_dates=['date'])

#prepare base map
'''Use mean of latitude and longitude in dataset and set original zoom'''
kingcounty_map = folium.Map(location = [houses['lat'].mean(),
	houses['long'].mean()], zoom_start = 10)
kingcounty_map.save('kingcounty_map.html')

#group together houses
house_groups = folium.MarkerCluster().add_to(kingcounty_map)

'''Iterate through rows and create marker clusters.
	popup datatypes:
		price: float64
		size: int64
		bedrooms: 1nt64
		bathrooms: float64
		year built: int64'''

for name, row in houses[0:200].iterrows():
    folium.Marker([row["lat"], row["long"]],
                  popup="Price: {0}$, Size: {1} sqft, Bedrooms: {2}, Bathrooms: {3}, Year Built: {4}"\
                  .format(row["price"], row['sqft_living'], row['bedrooms'], row['bathrooms'], row['yr_built'])).add_to(house_groups)

#save output of house markers
kingcounty_map.save('houses_map.html')

'''Create new basemap for crimes heat map'''
kccrimes_heatmap = folium.Map(location = [houses['lat'].mean(), houses['long'].mean()], zoom_start = 10)

'''Add data to heat map and select opacity'''
kccrimes_heatmap.add_children(
    plugins.HeatMap([[row["latitude"], row["longitude"],row["city"]]
    for iters, row in crimes[0:100].iterrows()],
    min_opacity=1, max_zoom=10, radius = 8))

#save output of King County heat map
kccrimes_heatmap.save('kingcounty_map.html')
