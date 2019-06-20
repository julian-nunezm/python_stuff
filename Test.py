import json

data = {"engineer": {"name":"Julian","lastname":"Nunez","age":31}}

#with open("data_file.json","w") as write_file:
#    json.dump(data, write_file)
#print (data)

json_string = json.dumps(data, indent=4)
print(json_string)

decoded = json.loads(json_string)
print(decoded)

#type(decoded)

with open("Alerts.json","r") as alerts_file:
    alerts = json.load(alerts_file)
#print(alerts)  #too long


