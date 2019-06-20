import json

print("-----------------ALERTS-----------------")

#Read the json file and load it to a Dictionary
with open("Alerts.json","r") as alerts_file:
    alerts = json.load(alerts_file)

alerts_by_type = {}
alerts_by_contentPackName = {}
alerts_by_info = {}

print(f"There are {len(alerts)} alerts.")

#Loop through all the alerts
for n in alerts:
    try:
        #Increment the existing alert type's count.
        alerts_by_type[n["alertType"]] += 1
    except KeyError:
        #Increment count to 1 if there is not a previous alert type.
        alerts_by_type[n["alertType"]] = 1
    try:
        #Increment the existing content pack name's count.
        alerts_by_contentPackName[n["contentPackName"]] += 1
    except KeyError:
        #Increment count to 1 if there is not a previous content pack name.
        alerts_by_contentPackName[n["contentPackName"]] = 1
    try:
        #Increment the existing info's count.
        alerts_by_info[n["info"]] += 1
    except KeyError:
        #Increment count to 1 if there is not a previous info.
        alerts_by_info[n["info"]] = 1

#Print the groups of alert types
print("\nAlerts by type")
for type in alerts_by_type:
    print(f"{type}: {alerts_by_type[type]}")
#Print the groups of content pack name
print("\nAlerts by Content Pack Name")
for packName in alerts_by_contentPackName:
    print(f"{packName}: {alerts_by_contentPackName[packName]}")
#Print the groups of info
print("\nAlerts by Info (More than 1 times")
for info in alerts_by_info:
    if alerts_by_info[info] > 1:
        print(f"{info[:70]}: {alerts_by_info[info]}")

print("\n\n")
print("-----------------EVENTS RESPONSE 1-----------------")

#Read the json file and load it to a Dictionary
with open("events-response-1.json","r") as response1_file:
    response1 = json.load(response1_file)

events_by_text = {}
#alerts_by_type = {}
#alerts_by_contentPackName = {}
#alerts_by_info = {}
seconds = response1['duration']/1000
events = response1['events']

print(f"There are {len(response1)} responses.")
print(f"The response spent {seconds} seconds.")
print(f"There are {len(events)} events.")

#Loop through all the events
for event in events:
    try:
        #Increment the existing alert type's count.
        events_by_text[event["text"]] += 1
    except KeyError:
        #Increment count to 1 if there is not a previous alert type.
        events_by_text[event["text"]] = 1
#    try:
#        #Increment the existing content pack name's count.
#        alerts_by_contentPackName[n["contentPackName"]] += 1
#    except KeyError:
#        #Increment count to 1 if there is not a previous content pack name.
#        alerts_by_contentPackName[n["contentPackName"]] = 1
#    try:
#        #Increment the existing info's count.
#        alerts_by_info[n["info"]] += 1
#    except KeyError:
#        #Increment count to 1 if there is not a previous info.
#        alerts_by_info[n["info"]] = 1

#Print the groups of event text
print("\nEvents by text")
for text in events_by_text:
    if events_by_text[text] > 1:
        print(f"{text}: {events_by_text[text]}")
#Print the groups of content pack name
#print("\nAlerts by Content Pack Name")
#for packName in alerts_by_contentPackName:
#    print(f"{packName}: {alerts_by_contentPackName[packName]}")
#Print the groups of info
#print("\nAlerts by Info (More than 1 times")
#for info in alerts_by_info:
#    if alerts_by_info[info] > 1:
#        print(f"{info[:70]}: {alerts_by_info[info]}")

