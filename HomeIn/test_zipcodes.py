from time import sleep
import unittest
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from zipcodes_search import *

zipcodes = []
locations = [("47.500626, -122.234039")]
class TestZipcodes(unittest.TestCase):
	def test_geocode(self):
		geocode()
       	result = '98178'
        self.assertEqual(zipcodes, result)

if __name__ == '__main__':
    unittest.main()