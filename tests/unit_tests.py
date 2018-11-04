import unittest
from convert_esri import *
import json



class TestMethods(unittest.TestCase):
	def test_get_esri_json__valid_url__more_than_one_row_returned(self):
		# Arrange

		# Act
		result = get_esri_json(NC_STATE_FAIR_ESRI_VENDOR_URL)
		#print(json.dumps(result, indent=3))

		# Assert
		self.assertGreater(len(result), 1)



	def test_convert_esri_json_to_csv__super_simple__header_and_row_returned(self):
		# Arrange
		input = {
			"displayFieldName": "NAMELABEL",
			"fieldAliases": {
				"OBJECTID": "OBJECTID",
				"FEATURETYPE": "FEATURETYPE",
				"CONTRACT": "CONTRACT",
				"NAMELABEL": "NAMELABEL",
				"LOT_LOC": "LOT_LOC",
				"EVENTPRO_LOT": "EVENTPRO_LOT",
				"LOC_NAME": "LOC_NAME",
				"DIMENSIONS": "DIMENSIONS",
				"MAP_PAGE": "MAP_PAGE",
				"INSPECTS": "INSPECTS",
				"DOL_NUM": "DOL_NUM",
				"SUB": "SUB",
				"CONTACT": "CONTACT",
				"CONTPHONE": "CONTPHONE",
				"TICKETS": "TICKETS",
				"PRODUCT": "PRODUCT",
				"URL": "URL",
				"VENDORTYPE": "VENDORTYPE",
				"ORIG_FID": "ORIG_FID"
			},
			"geometryType": "esriGeometryPoint",
			"spatialReference": {
				"wkid": 4326,
				"latestWkid": 4326
			},
			"fields": [{
				"name": "OBJECTID",
				"type": "esriFieldTypeOID",
				"alias": "OBJECTID"
			}, {
				"name": "FEATURETYPE",
				"type": "esriFieldTypeString",
				"alias": "FEATURETYPE",
				"length": 50
			}, {
				"name": "CONTRACT",
				"type": "esriFieldTypeString",
				"alias": "CONTRACT",
				"length": 254
			}, {
				"name": "NAMELABEL",
				"type": "esriFieldTypeString",
				"alias": "NAMELABEL",
				"length": 50
			}, {
				"name": "LOT_LOC",
				"type": "esriFieldTypeString",
				"alias": "LOT_LOC",
				"length": 20
			}, {
				"name": "EVENTPRO_LOT",
				"type": "esriFieldTypeString",
				"alias": "EVENTPRO_LOT",
				"length": 50
			}, {
				"name": "LOC_NAME",
				"type": "esriFieldTypeString",
				"alias": "LOC_NAME",
				"length": 50
			}, {
				"name": "DIMENSIONS",
				"type": "esriFieldTypeString",
				"alias": "DIMENSIONS",
				"length": 10
			}, {
				"name": "MAP_PAGE",
				"type": "esriFieldTypeString",
				"alias": "MAP_PAGE",
				"length": 12
			}, {
				"name": "INSPECTS",
				"type": "esriFieldTypeString",
				"alias": "INSPECTS",
				"length": 20
			}, {
				"name": "DOL_NUM",
				"type": "esriFieldTypeSmallInteger",
				"alias": "DOL_NUM"
			}, {
				"name": "SUB",
				"type": "esriFieldTypeString",
				"alias": "SUB",
				"length": 10
			}, {
				"name": "CONTACT",
				"type": "esriFieldTypeString",
				"alias": "CONTACT",
				"length": 50
			}, {
				"name": "CONTPHONE",
				"type": "esriFieldTypeString",
				"alias": "CONTPHONE",
				"length": 14
			}, {
				"name": "TICKETS",
				"type": "esriFieldTypeInteger",
				"alias": "TICKETS"
			}, {
				"name": "PRODUCT",
				"type": "esriFieldTypeString",
				"alias": "PRODUCT",
				"length": 750
			}, {
				"name": "URL",
				"type": "esriFieldTypeString",
				"alias": "URL",
				"length": 150
			}, {
				"name": "VENDORTYPE",
				"type": "esriFieldTypeString",
				"alias": "VENDORTYPE",
				"length": 50
			}, {
				"name": "ORIG_FID",
				"type": "esriFieldTypeInteger",
				"alias": "ORIG_FID"
			}],
			"features": [{
				"attributes": {
					"OBJECTID": 1,
					"FEATURETYPE": "Vendor",
					"CONTRACT": "Davis Concessions",
					"NAMELABEL": "Davis Con.",
					"LOT_LOC": "G-13.3",
					"EVENTPRO_LOT": "LOT G13.3",
					"LOC_NAME": "Grandstand",
					"DIMENSIONS": "20 X 29",
					"MAP_PAGE": "Page 7",
					"INSPECTS": "F&D",
					"DOL_NUM": "null",
					"SUB": "null",
					"CONTACT": "null",
					"CONTPHONE": "null",
					"TICKETS": "null",
					"PRODUCT": "Cotton Candy, Candy Apples, Caramel Corn & Confections",
					"URL": "null",
					"VENDORTYPE": "",
					"ORIG_FID": 1
				},
				"geometry": {
					"x": -78.71098,
					"y": 35.795005
				}
			}]
		}



		# Act
		result = convert_esri_json_to_csv(input)

		# Assert
		self.assertEqual(len(result), 2, "Expected single header and data row.")


if __name__ == '__main__':
	unittest.main()		


