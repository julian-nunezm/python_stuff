import csv, json, datetime as dt
from pprint import pprint
csv.field_size_limit(500000)

try:
    incidents = dict()
    inc = dict()
    i = 0
    paginationLimit = 1000
    incidentsLimit = [1000,5000,10000,15000,20000]
    for incLim in incidentsLimit:
        i = 0
        print(" ")
        print("Beginning to analyze "+ str(incLim) +" incidents...")
        with open('extract.csv', 'r', encoding="utf8") as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                #print(row)
                #print(i)
                incident = {}
                try:
                    if "Department of Environment, Land, Water and Planning" == row[5] or "Department of Economic Development, Jobs, Transport and Resources" == row[5]:
                        if i < incLim:
                            incident['Incident_Number'] = row[0]
                            incident['Summary'] = row[1]
                            incident['Notes'] = row[2]
                            #incident['STATUS'] = row[3]
                            #incident['priority'] = row[4]
                            #incident['Contact_Company'] = row[5]
                            #incident['Service_Type'] = row[8]
                            #incident['Reported_Source'] = row[10]
                            #incident['Reported_Date'] = row[11]
                            #incident['Resolved_Date'] = row[25]
                            #incident['Assigned_Group'] = row[18]
                            #incident['Owner_Group'] = row[22]
                            #incident['Owner'] = row[24]
                            #incident['z1D_Template_Name'] = row[26]
                            incident['Resolution'] = row[30]
                            #incident['Resolution_Method'] = row[31]
                            incidents[row[0]] = incident
                            i += 1
                            if(i%paginationLimit==0):
                                print(f"{i} incidents loaded")
                except Exception as e1:
                    print(f" - Error in row {i+1}: {str(e1)}")
                    print(type(row[25]))
                    print(row[25])
                    print(row[25][0])
                    print(f" -> Incident Number: {incident['Incident_Number']}, Ini Date: {incident['Reported_Date']}, End Date: {incident['Resolved_Date']}")
                    raise
        csvFile.close()
        print(f"There are {i} incidents read")

        #inc["INC000001877013"] = incidents["INC000001877013"]
        #inc["INC000001877017"] = incidents["INC000001877017"]
        #inc["INC000001861533"] = incidents["INC000001861533"]
        #inc["INC000001940152"] = incidents["INC000001940152"]
        #print(inc["INC000001861533"])
        #print(f"Printing JSON...")
        #print(json.dumps(inc))

        print(" ")
        print("Starting the checking of uncommon words...")
        print(" ")

        #incident = {}
        #incident['Incident_Number'] = '12345'
        #incident['Notes'] = "This is an outage, sentence"
        #inc['12345'] = incident
        #incident = {}
        #incident['Incident_Number'] = '12346'
        #incident['Notes'] = "This is another outage at Cenitex"
        #inc['12346'] = incident

        commonWordsLimit = [1,2,5,10,20]
        
        for cWordsLimit in commonWordsLimit:
            commonWords = []
            uncommonWords = []
            commonWordCounter = {}
            uncommonWordCounter = {}
            commonCounter = 0
            uncommonCounter = 0
            i = 0
            
            print("Looking for the most common "+ str(cWordsLimit) +"k words")
            txtFile = open(str(cWordsLimit) + 'k.txt', 'r', encoding="utf8")
            mostCommonWords = txtFile.read().split(",")
            txtFile.close()
            for k, v in incidents.items():    #inc or incidents
                notes = ""
                #print(v["Incident_Number"])
                notesWords = v["Notes"].split(" ")
                for n in notesWords:
                    existent = False
                    word = n.replace(":","").replace("-","").replace("'","").replace(".","").replace(",","").replace("(","").replace(")","").replace("*","")
                    commonWordCounter = {}
                    uncommonWordCounter = {}
                    if word.lower() in mostCommonWords:
                        commonCounter += 1
                        for cw in commonWords:
                            if word == cw["word"]:
                                cw["counter"] += 1
                                existent = True
                        if not existent:
                            commonWordCounter["word"] = word
                            commonWordCounter["counter"] = 1
                            commonWords.append(commonWordCounter)
                    else:
                        uncommonCounter += 1
                        #print(word)
                        for uw in uncommonWords:
                            if word == uw["word"]:
                                uw["counter"] += 1
                                existent = True
                        if not existent:
                            uncommonWordCounter["word"] = word
                            uncommonWordCounter["counter"] = 1
                            uncommonWords.append(uncommonWordCounter)
                if(i%paginationLimit==0):
                    print(f"{i} incidents notes already checked")
                i += 1
            print(f" - Common words: {commonCounter}")
            print(f" - Uncommon words: {uncommonCounter}")
            print(f" - Uncommon words percentage: {round((uncommonCounter/(commonCounter + uncommonCounter))*100, 2)}%")
            print("----------------------------------------------")
    #print("Common Words")
    #pprint(commonWords)
    #print("Not Common Words")
    #pprint(uncommonWords)
except Exception as e2:
    print(f" - Error: {str(e2)}")
