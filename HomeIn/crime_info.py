"""
This module is intended to return and output the crime information around
a given house gps within the cutoff distance
"""

from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from geopy.distance import vincenty

def crime_count(house_gps, crime_gps, crime_type, cutoff=1.0, output_plot=False):
    """
    Count and return a int of numbers of crimes (int) reports and a dictionary of
    grouped crime number, around a specifc house gps corrdinates
    within the cutoff distance. The crime information are also grouped and
    plotted as bar plot.

    Parameters
    ----------
    house_gps: list , default None, Latitude and Longtitude of the house
    crime_gps: tuple or list, default none, Latitudes and Longtitudes of the crime
    crime_type: list of strings, contains the types of crimes
    cutoff: float, default 1.0 mile, set up the range for counting
    output_plot: boolean, default False, decide if output a figure file of crimes
                with different type

    Return
    ----------
    count: int, total number of crimes within the cutoff distance
    counted_type: dictionary, grouped crimes number by their type, where type
                    names as keys, corresponding numbers as values
    """

    #count the total crime within the cutoff ranges
    count = 0
    count_type = []
    for i in range(0, len(crime_gps)):
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
    counted_type = dict(Counter(count_type))
    # output_plot data
    if output_plot:
        ax = crime_plot(counted_type)
        title = ('Crime Distribution Around The House Within '
                 + str(cutoff) + ' Mile(s), In Past 5 Years')
        plt.suptitle(title)
        plt.savefig('crime distribution')
    else:
        pass

    return (count, counted_type)

def crime_plot(plot_d):
    """
    Create and return a bar plot from input crime data

    Parameter
    ---------
    plot_d: dictionary, contains numbers (value) of grouped crimes(keys).

    Return
    ---------
    ax: a matplotlib type of bar plot based on the input dictionary
    """
    if sum(plot_d.values()) == 0.:
        print('There is no crime reports around the house within the cutoff'
              + ' distance in past 5 years')
    else:
        plot_dir = {k:v for k, v in plot_d.items() if v != 0.}
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.barh(range(len(plot_dir)), plot_dir.values(), align='center')
        plt.yticks(range(len(plot_dir)), plot_dir.keys())
        rects = ax.patches
        for rect in rects:
            length = rect.get_width()
            ax.text(length, rect.get_y() + rect.get_height()/2.,
                    '%d' % int(length), ha='left', va='center')
        return ax

def crime_info_output(house_gps, house_id, crime_gps, crime_type, cutoff=1.0,
                      output_csv=False, output_path='../Data/crime_info.csv'):
    """
    Output a pandas dataframe which contains information of house ids, total crime
    number, and grouped crime numbers by their type.

    Parameters
    ----------
    house_gps: tuple or list , default None, Latitude and Longtitudes of the house
    crime_gps: tuple or list, default none, Latitudes and Longtitudes of the crime
    crime_type: list of strings, contains the types of crimes
    cutoff: float, default 1.0 mile, set up the range for counting
    output_csv: boolean, default False, decide if output a csv file
    output_path: string, default "../Data/crime_info.csv", path and names of the
                output csv file if needed

    Return
    ----------
    df: pandas dataframe, nformation of house ids, total crime number, and
        grouped crime numbers by their type.

    """
    crime_type_list = list(set(crime_type))
    df_list = []

    for i in range(0, len(house_gps)-1):
        df_element = {}
        df_element['id'] = house_id[i]
        for j in crime_type_list:
            df_element[j] = 0.0

        counted_numb = 0
        grouped_crime = {}
        if np.isnan(house_gps[i][0]) or np.isnan(house_gps[i][1]):
            pass
        else:
            (counted_numb, grouped_crime) = crime_count(house_gps[i], crime_gps, crime_type, cutoff)
            for j in list(grouped_crime.keys()):
                df_element[j] = grouped_crime[j]
        df_element['number of crimes'] = counted_numb
        df_list.append(df_element)
    # rearrange the colums, making id and total number of crimes as first two columns
    df = pd.DataFrame(df_list)
    cols = df.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    df = df[cols]
    # output a csv file as user define
    if output_csv:
        df.to_csv(output_path)
    else:
        pass

    return df
