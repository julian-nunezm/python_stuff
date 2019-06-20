import csv, json, datetime as dt
csv.field_size_limit(500000)

try:
    incidents = dict()
    inc = dict()
    i = 0
    print("Beginning...")
    with open('extract.csv', 'r', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            #print(row)
            #print(i)
            incident = {}
            try:
                if "Department of Environment, Land, Water and Planning" == row[5] or "Department of Economic Development, Jobs, Transport and Resources" == row[5]:
                    incident['Incident_Number'] = row[0]
                    incident['Summary'] = row[1]
                    incident['Notes'] = row[2]
                    incident['STATUS'] = row[3]
                    #print(incident['STATUS'])
                    #incident['priority'] = row[4]
                    incident['Contact_Company'] = row[5]
                    #incident['Organization'] = row[6]
                    #incident['Department'] = row[7]
                    incident['Service_Type'] = row[8]
                    #incident['ServiceCI'] = row[9]
                    #incident['Reported_Source'] = row[10]
                    incident['Reported_Date'] = row[11]
                    incident['Resolved_Date'] = row[25]
                    #print(row[25])
                    #if row[25] is not "NULL":
                    #    incident['Time_Spent'] = dt.datetime.fromisoformat(str(row[25])) - dt.datetime.fromisoformat(str(row[11]))
                    #    #print(incident['Time_Spent'])
                    #else:
                    #    incident['Time_Spent'] = ""
                    #incident['Time_Spent'] = incident['Resolved_Date'] - incident['Reported_Date']
                    #incident['Categorization_Tier_1'] = row[12]
                    #incident['Categorization_Tier_2'] = row[13]
                    #incident['Categorization_Tier_3'] = row[14]
                    #incident['Product_Categorization_Tier_1'] = row[15]
                    #incident['Product_Categorization_Tier_2'] = row[16]
                    #incident['Product_Categorization_Tier_3'] = row[17]
                    #incident['Assigned_Group'] = row[18]
                    #incident['Assigned_Support_Company'] = row[19]
                    #incident['Assigned_Support_Organization'] = row[20]
                    #incident['Owner_Support_Organization'] = row[21]
                    #incident['Owner_Group'] = row[22]
                    #incident['Owner_Support_Company'] = row[23]
                    #incident['Owner'] = row[24]
                    #incident['z1D_Template_Name'] = row[26]
                    #incident['Attributed_To'] = row[27]
                    #incident['Service_Relief_Category'] = row[28]
                    #incident['CTX_Service_Relief_Category_Ev'] = row[29]
                    #incident['Resolution'] = row[30]
                    #incident['Resolution_Method'] = row[31]
                    #incident['Generic_Categorization_Tier_1'] = row[32]
                    #incident['Resolution_Category'] = row[33]
                    #incident['Resolution_Category_Tier_2'] = row[34]
                    #incident['Resolution_Category_Tier_3'] = row[35]
                    #incident['Closure_Product_Category_Tier1'] = row[36]
                    #incident['Closure_Product_Category_Tier2'] = row[37]
                    #incident['Closure_Product_Category_Tier3'] = row[38]
                    incidents[row[0]] = incident
                    if(i%50000==0):
                        print(f"Loading {i} incidents")
                    i += 1
            except Exception as e1:
                print(f" - Error in row {i+1}: {str(e1)}")
                print(type(row[25]))
                print(row[25])
                print(row[25][2])
                print(f" -> Incident Number: {incident['Incident_Number']}, Ini Date: {incident['Reported_Date']}, End Date: {incident['Resolved_Date']}")
                raise
    csvFile.close()
    print(f"There are {i} incidents read")

    inc["INC000001877013"] = incidents["INC000001877013"]
    inc["INC000001877017"] = incidents["INC000001877017"]
    inc["INC000001861533"] = incidents["INC000001861533"]
    inc["INC000001940152"] = incidents["INC000001940152"]
    #INC000001877013
    #INC000001877017
    #INC000001861533
    #INC000001940152
    #print(inc["INC000001861533"])
    print(f"Printing JSON...")
    print(json.dumps(inc))
    #try:
    #    print("Generating JSON file...")
    #    with open('stupidThing.json', 'w') as json_file:  
    #        json.dump(inc, json_file)
    #    print("JSON file done!")
    #except:
    #print("It's Yalda's fault!")
except Exception as e2:
    print(f" - Error: {str(e2)}")
