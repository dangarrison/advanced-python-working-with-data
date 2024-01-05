# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def getFelt(dataitem):
    felt = dataitem['properties']['felt']
    
    if (felt is None):
        felt = 0
    return int(felt)

def getSig(dataitem):
    sig = dataitem['properties']['sig']

    if (sig is None):
        sig = 0
    return int(sig)
    
quake = str(sum(quake['properties']['felt'] is not None and quake['properties']['felt'] >= 100
                                                       for quake in data['features']))


mostFeltQuake = max(data["features"], key=getFelt)


print(f"Total quakes: {len(data['features'])}")

print(f"Total quakes felt by at least 100 people: {quake}")

print(f"Most felt Reports: {mostFeltQuake['properties']['title']}, reports: {mostFeltQuake['properties']['felt']}")

data["features"].sort(key=getSig, reverse=True)

print(data["features"][0]['properties']['title'])

for i in range(0, 10):
    print(f"Event: {data['features'][i]['properties']['title']}, Significance: {data['features'][i]['properties']['sig']}")
