"""
This module is intended to return and output the crime information around
a given house gps
"""

from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from geopy.distance import vincenty

def crime_count(house_gps, crime_gps, crime_type,
                cutoff=1.0, crime_plot=False, house_name='the house'):
    """
    Count and return numbers of crimes (int) reports around a specifc house gps corrdinates
    within the cutoff distance. the crime information are also grouped and
    plotted as bar plot.

    Parameters
    ----------
    house_gps: list , default None, Latitude and Longtitude of the house
    crime_gps: tuple or list, default none, Latitudes and Longtitudes of the crime
    crime_type: list of strings, contains the types of crimes
    cutoff: float, default 1.0 mile, set up the range for counting
    crime_plot:
    house_name: string, default 'the house', contains the name of input house.
    """

    #count the total crime within the cutoff ranges
    count = 0
    count_type = []
    crime_total = len(crime_gps)
    for i in range(0, crime_total):
        if np.isnan(crime_gps[i][0]) or np.isnan(crime_gps[i][1]):
            pass
        else:
            distance = vincenty(house_gps, crime_gps[i]).miles
            if  distance <= cutoff:
                count += 1
                count_type.append(crime_type[i])
            else:
                pass

    #groupby the different types of crime
    counted_type = Counter(count_type)
    if crime_plot:
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(range(len(counted_type)), counted_type.values(), align='center')
        plt.xticks(range(len(counted_type)), counted_type.keys())
        title = 'Crime distribution around '+house_name+' within the range of '+str(cutoff)+' miles'
        plt.suptitle(title)
        plt.savefig('crime distribution')
    else:
        pass

    return (count, dict(counted_type))


if __name__ == "__main__":
    # Create an example to show the functionality of the module, based on house 1561
    HOUSE_DATA = pd.read_csv('../data/kc_house_data.csv')
    CRIME_DATA = pd.read_csv('../data/King_County_Sheriff_s_Office.csv')
    HOUSE_GPS = (HOUSE_DATA.lat[1561], HOUSE_DATA.long[1561])
    CRIME_LATS = list(CRIME_DATA.latitude)
    CRIME_LONS = list(CRIME_DATA.longitude)
    CRIME_GPS = list(zip(CRIME_LATS, CRIME_LONS))
    CRIME_TYPE = list(CRIME_DATA['incident_type_primary'])
    HOUSE_NAME = 'House NO. 1561'
    COUNT_HOUSE = crime_count(HOUSE_GPS, CRIME_GPS, CRIME_TYPE, house_name=HOUSE_NAME)
    print('Number of crime reports around ' + HOUSE_NAME +' is: ' + str(COUNT_HOUSE))
