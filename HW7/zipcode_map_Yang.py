# -*- coding: utf-8 -*-
"""
Folium interact with GeoJSON data
Examples: overlay another GeoJSON zipcode map to the original map
Author: Yang Jiang
"""

import pandas as pd
import folium

def show_zipcode_map(zipcode_path, data, col):
    """
    Interact zipcode GeoJSON data with other data set (house price or crime)
    and generate another layer of zipcode map onto the original map

    Parameters
    ----------
    path : string
        URL or File path to GeoJSON zipcode data

    data : pandas dataframe
        The other data set to interact with (house price or crime)

    col : string
        The colomn name in dataset to bound zipcode with
    """
    # Generate original map
    zipcode = folium.Map(location=[data['lat'].mean(), 
                                   data['long'].mean()], zoom_start=10)

    # Add zipcode map layer to orignial map
    zipcode.choropleth(geo_path=zipcode_path, data=data, 
                       columns=['zipcode', col], 
                       key_on='feature.properties.ZCTA5CE10', 
                       fill_color='OrRd', fill_opacity=0.5, line_opacity=0.2)
    zipcode.save('zipcode_' + col + '.html')
    return zipcode


if __name__ == "__main__":
    """
    Example of using show_zipcode_map funciton
    """

    # Load King County house price data
    house_data = pd.read_csv("../Data/kc_house_data.csv", 
                             parse_dates=['date'])
    house_data['zipcode'] = house_data['zipcode'].astype(str)

    # Group data by zipcode and calculate the mean value in each zipcode
    zipcode_data = pd.groupby(house_data, 'zipcode').mean()

    # Add new fields in dataset, the count of house sold in each zipcode
    zipcode_data['count'] = pd.groupby(house_data, 'zipcode').count()['id']
    zipcode_data.reset_index(inplace=True)

    # Path for GeoJSON zipcode data
    zipcodepath = '../Data/zipcode_king_county.geojson'
    show_zipcode_map(zipcodepath, zipcode_data, 'count')
    show_zipcode_map(zipcodepath, zipcode_data, 'price')
