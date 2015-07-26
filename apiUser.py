import requests


def main():

	results = requests.get("http://www.gw2spidy.com/api/v0.9/json/all-items/all").json()["results"]

	list = []

	for item in results:
		if item["offer_availability"] > 2000:
			list.append((item["name"], item["offer_availability"]))

	print list

main()