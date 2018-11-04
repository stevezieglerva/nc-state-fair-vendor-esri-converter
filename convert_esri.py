import requests
import io
import csv
import json



NC_STATE_FAIR_ESRI_VENDOR_URL = "https://www.ncmhtd.com/arcgis/rest/services/AG_SF/StateFairFRFapp/MapServer/1/query?returnGeometry=true&where=1%3D1&outSr=4326&outFields=*&inSr=4326&geometry={%22xmin%22%3A-78.717041015625%2C%22ymin%22%3A35.79108281624994%2C%22xmax%22%3A-78.7060546875%2C%22ymax%22%3A35.79999392988527%2C%22spatialReference%22%3A{%22wkid%22%3A4326}}&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&geometryPrecision=6&f=json"


def get_esri_json(url):
	response = requests.get(url)
	json_response = json.dumps(response.text)
	return json_response


def json_is_valid(input_json):
	if "displayFieldName" not in input_json:
		return False
	if "features" not in input_json:
		return False
	else:
		features = input_json["features"]
		if len(features) == 0:
			return False
	return True

def convert_esri_json_to_csv(input_json):
	csv_result = io.StringIO()
	writer = csv.writer(csv_result, quoting=csv.QUOTE_NONNUMERIC)

	count = 0
	header = {}
	header_list = []
	for feature in input_json["features"]:
		count = count + 1
		print(count)
		attributes = feature["attributes"]
		geometry = feature["geometry"]
		if count == 1:
			header = sorted(attributes.keys())
			header_list = list(header)
			header_list.append("x")
			header_list.append("y")
			writer.writerow(header_list)
		values_list = []
		for column in header:
			values_list.append(attributes[column])
		values_list.append(geometry["x"])
		values_list.append(geometry["y"])
		writer.writerow(values_list)	
	return csv_result.getvalue()


def main():
	vendor_json = get_esri_json(NC_STATE_FAIR_ESRI_VENDOR_URL)
	print("JSON Length:" + str(len(vendor_json)))
	print("JSON start:" + vendor_json[0:50])
	print(json.dumps(vendor_json, indent=3))
	csv_results = convert_esri_json_to_csv(vendor_json)
	print(csv_results)

if __name__ == '__main__':
	main()		

