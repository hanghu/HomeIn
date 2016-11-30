import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from geopy.distance import vincenty

def crime_count(house_gps, crime_gps, crime_type,
                    cutoff=2.0, house_name='the house'):
    """
    Count return numbers of crime reports around a specifc house gps corrdinates
        within the cutoff distance.

    Parameters
    ----------
    house_gps: list , default None, Latitude and Longtitude of the house
    crime_gps: tuple or list, default none, Latitudes and Longtitudes of the crime
    crime_type: list of strings, contains the types of crimes
    cutoff: float, default 2.0, set up the rang for counting
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
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(range(len(counted_type)), counted_type.values(), align='center')
    plt.xticks(range(len(counted_type)), counted_type.keys())
    title = 'Crime distribution around '+house_name+' within the range of '+str(cutoff)+' miles'
    plt.suptitle(title)
    plt.savefig('crime distribution')
    return count

# showing an example of this function
house_data = pd.read_csv('../data/kc_house_data.csv')
crime_data = pd.read_csv('../data/King_County_Sheriff_s_Office.csv')
house_gps = house_gps = (crime_data.latitude[1561], crime_data.longitude[1561])
crime_lats = list(crime_data.latitude)
crime_lons = list(crime_data.longitude)
crime_gps = list(zip(crime_lats,crime_lons))
crime_type = list(crime_data['incident_type_primary'])
house_name = 'House NO. 1561'
count_house1561 = crime_count(house_gps, crime_gps, crime_type, house_name=house_name)
print('Number of crime reports around ' + house_name +' is: ' + str(count_house1561))
