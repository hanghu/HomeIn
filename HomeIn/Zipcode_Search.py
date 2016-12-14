'''This is a module for finding zipcodes from addresses generated through geocoding'''

from time import sleep
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim


#load crime data
crimes = pd.read_csv('../data/cleaned_crime_data.csv')

#eliminate crimes with no gps coordinates
crimes = crimes[crimes.latitude != 0]
crimes = crimes[crimes.longitude != 0]
crimes = crimes[np.isfinite(crimes['longitude'])]


#define variables for zipcode recursion
locations = list(zip(crimes.latitude, crimes.longitude))
zipcodes = []
geolocator = Nominatim()

def geocode():
    '''Recursion to find all zipcodes from gecoded address data'''
    for item in locations:
        location = geolocator.reverse(item, timeout=10)
        address = location.address
        split1 = address.rsplit(', ', 1)
        split2 = split1[0]
        split3 = split2.rsplit(', ', 1)
        zipcode = split3[1]
        zipcodes.append(zipcode)
        #sleep(1) is used because Nominatim() requires 1 second between requests
        sleep(1)
geocode()

#Showing example of one instance
location = geolocator.reverse("47.500626, -122.234039")
add = location.address
splita = add.rsplit(', ', 1)
splitb = splita[0]
splitc = splitb.rsplit(', ', 1)
code = splitc[1]
