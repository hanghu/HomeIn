# -*- coding: utf-8 -*-
"""
@author: Yang
General Map Demo based on the selection layers
"""

import pandas as pd
import folium
from folium import plugins
import house_cluster as hc

def generate_map(marker_layer=True, marker_num=None, crime_heatmap=True, choropleth_zipcode=True):
    """
    Funtion to generate map demo

    Input:
        marker_layer --- bool, whether to generate marker for each house
        marker_num --- number of markers to generate in the map,
        if None, all the markers will generate
        crime_heatmap --- bool, whether to generate a map of crime incidence
        choropleth_zipcode --- bool, choropleth layer of average house price in each zipcode
    return a html file
    """
    data = pd.read_csv("../Data/house_crime_data.csv", parse_dates=['date'])
    data['zipcode'] = data['zipcode'].astype(str)
    crime_data = pd.read_csv('../Data/cleaned_crime_data.csv',
                             parse_dates=['incident_datetime'])
    zipcode_data = data.groupby('zipcode').mean()
    zipcode_data['count'] = data.groupby('zipcode').count()['id']
    zipcode_data.reset_index(inplace=True)
    # Generate base map layer
    geo_path = '../Data/zipcode_king_county.geojson'
    Map = folium.Map(location=[data['lat'].mean(),
                               data['long'].mean()], zoom_start=11, API_key='zipcode')
    # Generate marker map layer
    if marker_layer == True:
        if marker_num is not None:
            MAX_SHOW = marker_num
            marker_cluster = folium.MarkerCluster(name='House Cluster').add_to(Map)
            for iters, row in data[0:MAX_SHOW].iterrows():
                folium.Marker([row["lat"], row["long"]],
                              popup=hc.popup_text(iters, row)).add_to(marker_cluster)
        else:
            marker_cluster = folium.MarkerCluster(name='House Cluster').add_to(Map)
            for iters, row in data.iterrows():
                folium.Marker([row["lat"], row["long"]],
                              popup=hc.popup_text(iters, row)).add_to(marker_cluster)
    # Generate zipcode vs. house price layer
    if choropleth_zipcode == True:
        Map.choropleth(geo_path=geo_path, data=zipcode_data,
                       columns=['zipcode', 'price'], key_on='feature.properties.ZCTA5CE10',
                       fill_color='OrRd', threshold_scale=[200000, 400000, 600000, 800000,
                                                           1000000, 1500000], fill_opacity=0.6,
                       line_opacity=0.2, legend_name='House Price')

    # Generate Crime heatmap
    if crime_heatmap == True:
        Map.add_children(plugins.HeatMap([[row["latitude"], row["longitude"]]
                                          for iters, row in crime_data.iterrows()],
                                         name='Crime Incidence', min_opacity=0.5,
                                         max_zoom=18, radius=11))


    folium.LayerControl().add_to(Map)
    Map.save('Map.html')

if __name__ == "__main__":
    generate_map(marker_layer=True, marker_num=1, crime_heatmap=True, choropleth_zipcode=True)
    