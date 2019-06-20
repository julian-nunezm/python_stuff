import csv, json

f = open('Incidents.xlsx','r')
fieldnames = ("Incident_Number","Template_Name","Assigned_Group",
              "Reported_Source","Service_Type","Department",
              "Submit_Date","Last_Resolved_Date")

reader = csv.DictReader(f, fieldnames)

store = []
framenames = []

#Store framenames in a list
for row in reader:
    frame = {"Incident Number":row["Incident_Number"]}

print(frame)
