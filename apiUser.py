import requests


def main():
	url = "https://api.guildwars2.com/v2/commerce/listings/"

	result = requests.get(url).json()
	print "NUMBER OF IDS: " + str(len(result))

	list = []

	for id in result:
		newUrl = url + str(id)
		itemListings = requests.get(newUrl).json()
		print "TRYING " + str(id)
		print "LISTINGS: " + str(getNumberOfListings(itemListings))
		if getNumberOfListings(itemListings) > 2000:
			list.append(id)


	print "DONE"
	print list



def getNumberOfListings(item):
	total = 0
	buys = item["buys"]
	for d in buys:
		total += d["listings"]
	return total 


main()