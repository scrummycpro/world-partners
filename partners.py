import json


with open('factbook.json','r') as blue:
	data = json.load(blue)

z = str(raw_input("ENTER COUNTRY: "))
print(" ")

print("Imported Commodities")

print("*"*20)

for imported in data['countries'][z]['data']['economy']['imports']['commodities']['by_commodity']:
	print(imported)

print("*"*20)

print("""

The Import Trading Partners for %s are:

"""%(z.title()))

for i in range(4):

	print(data['countries'][z]['data']['economy']['imports']['partners']['by_country'][i]['name'])

print("-"*10)

print("Exported Commodities")

print("*"*20)

for exported in data['countries'][z]['data']['economy']['exports']['commodities']['by_commodity']:
	print(exported)

print("*"*20)

print("""

The Export Trading Partners for %s are:

"""%(z.title()))

for i in range(4):

	print(data['countries'][z]['data']['economy']['exports']['partners']['by_country'][i]['name'])







