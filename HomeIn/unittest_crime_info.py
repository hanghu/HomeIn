"""unit tests for crime_info"""
import unittest
import os.path as op
import requests
import pandas as pd
import numpy as np
from crime_info import crime_count
from crime_info import crime_plot
from crime_info import crime_info_output

#load sample data for testing
house_data = pd.read_csv()
crime_data = pd.read_csv(crime_data_path)
crime_type = list(crime_data['incident_type_primary'])
crime_lats = list(crime_data.latitude)
crime_lons = list(crime_data.longitude)
crime_gps = list(zip(crime_lats,crime_lons))
house_lat = list(house_data.lat)
house_long = list(house_data.long)
house_gps_test = list(zip(house_gps_lat[0:10], house_data.long[0:10]))
crime_gps_test = crime_gps[0:10000]
house_id_test = list(house_data.id[0:10])
crime_type_test = crime_type[0:10000]

class TestCrimeInfo(unittest.TestCase):
    """tests the three function in crime_info"""
    # test crime_count
    def testcountoutput(self):
        """test the output of crime_count"""
        (total_numb, grouped_crime) = crime_count(house_gps_test[0],
                                                  crime_gps, crime_type)
        result = (type(total_numb) == int)
        self.assertTrue(result)
        result = (type(grouped_crime) == dict)
        self.assertTrue(result)

    def testcountcutoff(self):
        (total_numb, grouped_crime) = crime_count(house_gps_test[0],
                                                  crime_gps, crime_type)
        (total_numb_1, grouped_crime_1) = crime_count(house_gps_test[0], crime_gps,
                                                      crime_type, cutoff=100.0)
        result = (total_numb != total_numb_1)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
