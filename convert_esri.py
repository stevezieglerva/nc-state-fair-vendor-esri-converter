import requests
import io
import csv
import json


NC_STATE_FAIR_ESRI_VENDOR_URL = "https://www.ncmhtd.com/arcgis/rest/services/AG_SF/StateFairFRFapp/MapServer/1/query?returnGeometry=true&where=1%3D1&outSr=4326&outFields=*&inSr=4326&geometry={%22xmin%22%3A-78.717041015625%2C%22ymin%22%3A35.79108281624994%2C%22xmax%22%3A-78.7060546875%2C%22ymax%22%3A35.79999392988527%2C%22spatialReference%22%3A{%22wkid%22%3A4326}}&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&geometryPrecision=6&f=json"


def get_esri_json(url):
	response = requests.get(url)
	json_response = json.dumps(response.text)
	return json_response


def convert_esri_json_to_csv(input_json):
	result = {}

	count = 0
	for feature in input_json["features"]:
		count = count + 1
		print(count)


	return result


