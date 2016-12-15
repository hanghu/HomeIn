from time import sleep
import unittest
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from zipcodes_search import *


class TestZipcodes(unittest.TestCase):
	def test_geocode(self):
		location = geolocator.reverse("47.500626, -122.234039")
		add = location.address
		splita = add.rsplit(', ', 1)
		splitb = splita[0]
		splitc = splitb.rsplit(', ', 1)
		code = splitc[1]
       	result = '98178'
        self.assertEqual(code, result)

if __name__ == '__main__':
    unittest.main()