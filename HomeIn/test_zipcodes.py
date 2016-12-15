import unittest
from geopy.geocoders import Nominatim

class TestZipcodes(unittest.TestCase):

	def testgeocode(self):
		'''Test an instance of zipcode retrieval'''
		geolocator = Nominatim()
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