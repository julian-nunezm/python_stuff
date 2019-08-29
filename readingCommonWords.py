import csv, json, datetime as dt, time
from pprint import pprint
csv.field_size_limit(500000)

try:
    start = time.time()
    incidents = dict()
    inc = dict()
    i = 0
    paginationLimit = 1000
    incidentsLimit = [5000]   #[1000,2000,5000,10000,20000,50000,100000]
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

        commonWordsLimit = [1]
        #ToDo: Count reset and Reset as the same word
        for cWordsLimit in commonWordsLimit:
            commonWords = []
            uncommonWords = []
            cenitexWords = []
            commonWordCounter = {}
            cenitexWordCounter = {}
            uncommonWordCounter = {}
            commonCounter = 0
            cenitexCounter = 0
            uncommonCounter = 0
            i = 0
            print("Looking for the most common "+ str(cWordsLimit) +"k words")
            #Loading most common words in English
            txtFile = open(str(cWordsLimit) + 'k.txt', 'r', encoding="utf8")
            mostCommonWords = txtFile.read().split(",")
            txtFile.close()
            #Loading Cenitex words
            txtFile = open('cenitex.txt', 'r', encoding="utf8")
            commonCenitexWords = txtFile.read().split(",")
            txtFile.close()
            for k, v in incidents.items():    #inc or incidents
                #Summary
                #print("Analyzing incidents Summary")
                notes = ""
                #print(v["Incident_Number"])
                notesWords = v["Notes"].replace(":","").replace("-","").replace("'","").replace(".","").replace(",","").replace("(","").replace(")","").replace("*","").replace("=","").replace("|","").replace("&","").replace("?","").split(" ")
                #ToDo: Compare not only Summary, but also Worlog, Resolution and more! Maintain the same counters!
                for word in notesWords:
                    existent = False
                    #ToDo: Check if it's better to replace the whole Notes instead of each word!
                    #word = n.replace(":","").replace("-","").replace("'","").replace(".","").replace(",","").replace("(","").replace(")","").replace("*","").replace("=","").replace("|","").replace("&","")
                    commonWordCounter = {}
                    cenitexWordCounter = {}
                    uncommonWordCounter = {}
                    if word != "" and word not in ["0","1","2","3","4","5","6","7","8","9","-"] and "http/" not in word:
                        if word.lower() in mostCommonWords:
                            for cw in commonWords:
                                if word.lower() == cw["word"]:
                                    cw["counter"] += 1
                                    existent = True
                            if not existent:
                                commonWordCounter["word"] = word.lower()
                                commonWordCounter["counter"] = 1
                                commonWords.append(commonWordCounter)
                                commonCounter += 1
                        #ToDo: Count Cenitex jargon words
                        elif word.lower() in commonCenitexWords:
                            for cw in cenitexWords:
                                if word.lower() == cw["word"]:
                                    cw["counter"] += 1
                                    existent = True
                            if not existent:
                                cenitexWordCounter["word"] = word.lower()
                                cenitexWordCounter["counter"] = 1
                                cenitexWords.append(cenitexWordCounter)
                                cenitexCounter += 1
                        else:
                            for uw in uncommonWords:
                                if word.lower() == uw["word"]:
                                    uw["counter"] += 1
                                    existent = True
                            if not existent:
                                uncommonWordCounter["word"] = word.lower()
                                uncommonWordCounter["counter"] = 1
                                uncommonWords.append(uncommonWordCounter)
                                uncommonCounter += 1
                #Resolution
                #print("Analyzing incidents Resolution")
                resolution = ""
                #print(v["Incident_Number"])
                resolutionWords = v["Resolution"].replace(":","").replace("-","").replace("'","").replace(".","").replace(",","").replace("(","").replace(")","").replace("*","").replace("=","").replace("|","").replace("&","").replace("?","").split(" ")
                for r in resolutionWords:
                    existent = False
                    #word = r.replace(":","").replace("-","").replace("'","").replace(".","").replace(",","").replace("(","").replace(")","").replace("*","").replace("=","").replace("|","").replace("&","")
                    commonWordCounter = {}
                    cenitexWordCounter = {}
                    uncommonWordCounter = {}
                    if word != "" and word not in ["0","1","2","3","4","5","6","7","8","9","-"] and "http/" not in word:
                        if word.lower() in mostCommonWords:
                            for cw in commonWords:
                                if word.lower() == cw["word"]:
                                    cw["counter"] += 1
                                    existent = True
                            if not existent:
                                commonWordCounter["word"] = word.lower()
                                commonWordCounter["counter"] = 1
                                commonWords.append(commonWordCounter)
                                commonCounter += 1
                        #ToDo: Count Cenitex jargon words
                        elif word.lower() in commonCenitexWords:
                            for cw in cenitexWords:
                                if word.lower() == cw["word"]:
                                    cw["counter"] += 1
                                    existent = True
                            if not existent:
                                cenitexWordCounter["word"] = word.lower()
                                cenitexWordCounter["counter"] = 1
                                cenitexWords.append(cenitexWordCounter)
                                cenitexCounter += 1
                        else:
                            for uw in uncommonWords:
                                if word.lower() == uw["word"]:
                                    uw["counter"] += 1
                                    existent = True
                            if not existent:
                                uncommonWordCounter["word"] = word.lower()
                                uncommonWordCounter["counter"] = 1
                                uncommonWords.append(uncommonWordCounter)
                                uncommonCounter += 1
                i += 1
                if(i%paginationLimit==0):
                    print(f"{i} incidents Summary and Resolution fields already checked")
            print(f" - Common words: {commonCounter}")
            print(f" - Cenitex words: {cenitexCounter}")
            print(f" - Uncommon words: {uncommonCounter}")
            print(f" - Cenitex words percentage: {round((cenitexCounter/(commonCounter + cenitexCounter + uncommonCounter))*100, 2)}%")
            print(f" - Uncommon words percentage: {round((uncommonCounter/(commonCounter + cenitexCounter + uncommonCounter))*100, 2)}%")
            print("----------------------------------------------")
            #pprint(sorted(uncommonWords,key=lambda i: i["counter"], reverse = True))
    elapsed = time.time() - start
    print(f"Time: {round(elapsed,2)} seconds")
    #print("Common Words")
    #pprint(commonWords)
    #print("Not Common Words")
    #pprint(uncommonWords)
except Exception as e2:
    print(f" - Error: {str(e2)}")
