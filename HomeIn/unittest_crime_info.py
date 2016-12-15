"""unit tests for crime_info"""
import unittest
import os
import sys
from io import StringIO
import requests
import pandas as pd
import numpy as np
from crime_info import crime_count
from crime_info import crime_plot
from crime_info import crime_info_output

#load sample data for testing
house_data = pd.read_csv('../data/kc_house_data.csv')
crime_data = pd.read_csv('../data/cleaned_crime_data.csv')
crime_type = list(crime_data['incident_type_primary'])
crime_lats = list(crime_data.latitude)
crime_lons = list(crime_data.longitude)
crime_gps = list(zip(crime_lats,crime_lons))
house_lat = list(house_data.lat)
house_long = list(house_data.long)
house_gps_test = list(zip(house_lat[0:10], house_long[0:10]))
crime_gps_test = crime_gps[0:10000]
house_id_test = list(house_data.id[0:10])
crime_type_test = crime_type[0:10000]

class TestCrimeInfo(unittest.TestCase):
    """tests the three function in crime_info"""
    # test crime_count
    def testcountreturns(self):
        """test the returns of crime_count"""
        (total_numb, grouped_crime) = crime_count(house_gps_test[0],
                                                  crime_gps, crime_type)
        result = (type(total_numb) == int)
        self.assertTrue(result)
        result = (type(grouped_crime) == dict)
        self.assertTrue(result)

    def testcountcutoff(self):
        """test the cutoff parameter of crime_count"""
        (total_numb, grouped_crime) = crime_count(house_gps_test[0],
                                                  crime_gps, crime_type)
        (total_numb_1, grouped_crime_1) = crime_count(house_gps_test[0], crime_gps,
                                                      crime_type, cutoff=100.0)
        result = (total_numb != total_numb_1)
        self.assertTrue(result)

    def testcountoutput(self):
        """test the output barplot of crime_count"""
        if os.path.exists('crime_distribution.png'):
            os.remove('crime_distribution.png')
        (total_numb_1, grouped_crime_1) = crime_count(house_gps_test[0], crime_gps_test,
                                                      crime_type_test, output_plot=True)
        result = os.path.exists('crime_distribution.png')
        self.assertTrue(result)
        if os.path.exists('crime_distribution.png'):
            os.remove('crime_distribution.png')
    # test crime_plot
    def testplotwithnocrime(self):
        """test the no crime case for crime_plot"""
        a = {'a':0. ,'b':0. ,'c':0.}
        out = StringIO()
        sys.stdout = out
        crime_plot(a)
        result = out.getvalue().strip()
        printed_info =('There is no crime reports around the house within the cutoff'
                       + ' distance in past 5 years')
        self.assertEqual(result, printed_info)

    def testplotreturns(self):
        """test the type of return variable as the matplotlib subplot in crime_plot"""
        a = {'a':1. ,'b':2. ,'c':3.}
        result = crime_plot(a)
        type_name = "<class 'matplotlib.axes._subplots.AxesSubplot'>"
        self.assertEqual(str(type(result)), type_name)
    # test crime_info_output
    def testoutputreturn(self):
        """test the type of return variable as pandas dataframe in crime_info_output"""
        result = crime_info_output(house_gps_test, house_id_test, crime_gps_test,
                                   crime_type_test)
        type_name = "<class 'pandas.core.frame.DataFrame'>"
        self.assertEqual(str(type(result)), type_name)

    def testoutputcsv(self):
        """test the output_cav function of crime_info_output"""
        if os.path.exists('result.csv'):
            os.remove('result.csv')
        df = crime_info_output(house_gps_test, house_id_test, crime_gps_test,
                                   crime_type_test, output_csv=True,
                                   output_path="./result.csv")
        result = os.path.exists('result.csv')
        self.assertTrue(result)
        if os.path.exists('result.csv'):
            os.remove('result.csv')

if __name__ == '__main__':
    unittest.main()
