import unittest
from convert_esri import *



class TestMethods(unittest.TestCase):
	def test_get_esri_json__valid_url__more_than_one_row_returned(self):
		# Arrange

		# Act
		result = get_esri_json()

		# Assert
		self.assertGreater(len(result), 1)




if __name__ == '__main__':
	unittest.main()		


