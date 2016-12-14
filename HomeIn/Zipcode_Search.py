import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from time import sleep

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

#use recursion to find all zipcodes for data
def geocode():
    for item in locations[0:10]:
        location = geolocator.reverse(item, timeout=10)
        x = location.address
        z = x.rsplit(', ', 1)
        r = z[0]
        s = r.rsplit(', ', 1)
        zipcode = s[1]
        zipcodes.append(zipcode)
        #sleep(1) is used because Nominatim() requires 1 second between requests
        sleep(1)
geocode()

