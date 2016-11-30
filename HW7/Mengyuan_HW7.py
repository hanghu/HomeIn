import os

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import folium 
from folium import plugins
import webbrowser


# Set global settings and macros.
MAX_SHOW =10000
HOUSE_URL = 'houses.html'
HOUSE_HEAT_URL = "househeatmap.html"
CRIME_HEAT_URL = "crimeheatmap.html"
pd.set_option('display.max_columns', None) # To display all columns


# Read in king county house data.
data = pd.read_csv("../../Data/kc_house_data.csv", parse_dates = ['date'])
data['zipcode'] = data['zipcode'].astype(str)

## Create one map shwoing each listing of in house dataset and show in browser.

# Use folium Map function to plot underlying basic map.
houses_map = folium.Map(location = [data['lat'].mean(), data['long'].mean()], zoom_start = 10)
# Define clusters to show house clusters to add to the underlying houses_map.
marker_cluster = folium.MarkerCluster().add_to(houses_map)
# Iteratively add interactive clusters to the basic map.
#	When mouse-over the cluster, show house listing information:
#	sqft, price.
for iters, row in data[0:MAX_SHOW].iterrows():
    folium.Marker([row["lat"], row["long"]], 
                  popup="{0} sqft:  Sold for $ {1}"\
                  .format(row["sqft_living"], row["price"])).add_to(marker_cluster)

# Save the house cluster map to a html and open it in broswer.
houses_map.save(HOUSE_URL)
webbrowser.open('file://' + os.path.realpath(HOUSE_URL),new=2)

## Create one map showing the frequency of house sales and show in browser.

# Use folium Map function to plot underlying basic map.
houses_heatmap = folium.Map(location = [data['lat'].mean(), data['long'].mean()], zoom_start = 10)
# Add heatmap on top of the basic map.
houses_heatmap.add_children(
        plugins.HeatMap([[row["lat"], row["long"],row["price"]] 
            for iters, row in data.iterrows()],
            	min_opacity=0.5, max_zoom=18, radius = 8)) #[0:MAX_SHOW]

# Save the house sale frequency heat map to a html and open it in broswer.
houses_heatmap.save(HOUSE_HEAT_URL)
webbrowser.open('file://' + os.path.realpath(HOUSE_HEAT_URL),new=2)



