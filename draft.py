import json

array = []

#Read the json file and load it to a Dictionary
with open("Alerts.json","r") as alerts_file:
    alerts = json.load(alerts_file)

#Loop through all the alerts
for alert in alerts:
    alerts_detail = {}
    alerts_detail["id"] = alert["id"]
    alerts_detail["alertType"] = alert["alertType"]
    alerts_detail["name"] = alert["name"]
    alerts_detail["info"] = alert["info"]
    alerts_detail["contentPackNamespace"] = alert["contentPackNamespace"]
    alerts_detail["contentPackName"] = alert["contentPackName"]
    #print(alerts_detail)
    array.append(alerts_detail)
    #print(len(array))

print(f"There are {len(array)} alerts.")
#print(array)

#for n in array:
    #print(f"Id: {n['id']}")
    #print(f"Alert Type: {n['alertType']}")
    #print(f"Name: {n['name']}")
    #print(f"Info: {n['info']}")
    #print(f"Content Pack Namespace: {n['contentPackNamespace']}")
    #print(f"Content Pack Name: {n['contentPackName']}")
    #print("---------------------------------")

alerts_by_type = {}
alerts_by_contentPackName = {}
alerts_by_info = {}

for n in alerts:
    try:
        #Increment the existing user's count.
        alerts_by_type[n["alertType"]] += 1
    except KeyError:
        #This user has not been seen. Set their count to 1.
        alerts_by_type[n["alertType"]] = 1
    try:
        #Increment the existing user's count.
        alerts_by_contentPackName[n["contentPackName"]] += 1
    except KeyError:
        #This user has not been seen. Set their count to 1.
        alerts_by_contentPackName[n["contentPackName"]] = 1
    try:
        #Increment the existing user's count.
        alerts_by_info[n["info"]] += 1
    except KeyError:
        #This user has not been seen. Set their count to 1.
        alerts_by_info[n["info"]] = 1

print("\nAlerts by type")
for type in alerts_by_type:
    print(f"{type}: {alerts_by_type[type]}")
print("\nAlerts by Content Pack Name")
for packName in alerts_by_contentPackName:
    print(f"{packName}: {alerts_by_contentPackName[packName]}")
print("\nAlerts by Info (More than 1 times")
for info in alerts_by_info:
    if alerts_by_info[info] > 1:
        print(f"{info[:70]}: {alerts_by_info[info]}")
