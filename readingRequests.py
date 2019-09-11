import csv, json, datetime as dt, time
from pprint import pprint
from tensorflow.keras.preprocessing.text import text_to_word_sequence as ttws
csv.field_size_limit(500000)
#https://github.com/first20hours/google-10000-english/blob/master/20k.txt

commonCounter = 0
cenitexCounter = 0
uncommonCounter = 0
paginationLimit = 5000
incidentsLimit = [20000]   #[1000,2000,5000,10000,20000,50000,100000]
words = 0

def filterText (incident, field):
    cleanWords = set(ttws(incident[field])) 
    for word in cleanWords:
        existent = False
        wordsDictCounter = {}
        commonWordCounter = {}
        cenitexWordCounter = {}
        uncommonWordCounter = {}
        #ToDo: Create also a function to look for any word to show which pool the word is in.
        #if word != "" and word not in ["0","1","2","3","4","5","6","7","8","9","-", ">"] and "http/" not in word: #Already done by keras function
        for w in wordsArray:
            if word.lower() == w["word"]:
                w["counter"] += 1
                existent = True
        if not existent:
            wordsDictCounter["word"] = word.lower()
            wordsDictCounter["counter"] = 1
            wordsArray.append(wordsDictCounter)
        global words
        words += 1
        #else:
            #print(word)

def printCommonWords():
    pprint(sorted(commonWords,key=lambda i: i["counter"], reverse = True))

def printCenitexWords():
    pprint(sorted(cenitexWords,key=lambda i: i["counter"], reverse = True))

def printUncommonWords():
    pprint(sorted(uncommonWords,key=lambda i: i["counter"], reverse = True))

def printWords():
    pprint(sorted(wordsArray,key=lambda i: i["counter"], reverse = True))

def setElapsedTime (elapsed):
    if elapsed > 60:
        elapsed /= 60
        if elapsed > 60:
            return str(round(elapsed/60,2))+" hours"
        else:
            return str(round(elapsed,2))+" minutes"
    else:
        return str(round(elapsed,2))+" seconds"

try:
    start = time.time()
    incidents = dict()
    inc = dict()
    for incLim in incidentsLimit:
        i = 0
        print(" ")
        print("Beginning to analyze "+ str(incLim) +" requests...")
        with open('requests_data.csv', 'r', encoding="utf8") as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                incident = {}
                try:
                    #print("Tier 1: " + row[9] + " - Number: " + row[1])
                    if i < incLim:
                        #print("Tier 1: " + row[9])
                        if row[9] == "Request":
                            #print("Tier 1: " + row[9] + " - Number: " + row[1])
                            #ToDo: Try make the analysis here to avoid more extra loops
                            #ToDo: Check what other columns should be read!
                            incident['Incident_Number'] = row[1]
                            incident['Summary'] = row[4]
                            incident['Operational_Categorization_Tier 1'] = row[9]
                            incident['Operational_Categorization_Tier 2'] = row[10]
                            incident['Operational_Categorization_Tier 3'] = row[11]
                            incidents[row[1]] = incident
                        i += 1
                        if(i%paginationLimit==0):
                            print(f"{i} requests loaded")
                    else:
                        break
                except Exception as e1:
                    print(f" - Error in row {i+1}: {str(e1)}")
                    #print(type(row[25]))
                    #print(row[25])
                    #print(row[25][0])
                    #print(f" -> Incident Number: {incident['Incident_Number']}, Ini Date: {incident['Reported_Date']}, End Date: {incident['Resolved_Date']}")
                    print(f" -> Incident Number: {incident['Incident_Number']}")
                    raise
        csvFile.close()
        print(f"There are {i} requests read")

        """
        inc["INC000001877013"] = incidents["INC000001877013"]
        inc["INC000001877017"] = incidents["INC000001877017"]
        inc["INC000001861533"] = incidents["INC000001861533"]
        inc["INC000001940152"] = incidents["INC000001940152"]
        print(inc["INC000001861533"])
        print(f"Printing JSON...")
        print(json.dumps(inc))
        """

        print(" ")
        print("Analyzing requests...")
        print(" ")

        """
        incident = {}
        incident['Incident_Number'] = '12345'
        incident['Notes'] = "This is an outage, sentence"
        inc['12345'] = incident
        incident = {}
        incident['Incident_Number'] = '12346'
        incident['Notes'] = "This is another outage at Cenitex"
        inc['12346'] = incident
        """

        commonWordsLimit = [1]
        for cWordsLimit in commonWordsLimit:
            wordsArray = []
            commonWords = []
            uncommonWords = []
            cenitexWords = []
            wordsDictCounter = {}
            commonWordCounter = {}
            cenitexWordCounter = {}
            uncommonWordCounter = {}
            i = 0
            totalWords = 0
            """print("Looking for the most common "+ str(cWordsLimit) +"k words")
            #Loading most common words in English
            txtFile = open(str(cWordsLimit) + 'k.txt', 'r', encoding="utf8")
            mostCommonWords = txtFile.read().split(",")
            txtFile.close()"""
            """#Loading Cenitex words
            txtFile = open('cenitex.txt', 'r', encoding="utf8")
            commonCenitexWords = txtFile.read().split(",")
            txtFile.close()"""
            for k, v in incidents.items():    #inc or incidents
                filterText(v, "Summary")
                i += 1
                if(i%paginationLimit==0):
                    print(f"{i} requests fields already checked")
            print("----------------------------------------------")
            print("Results:")
            print("----------------------------------------------")
            print(f" - Total words analyzed: {words}")
            #totalCounter = commonCounter + cenitexCounter + uncommonCounter
            #print(f" - Common words: {commonCounter}")
            #print(f" - Cenitex words: {cenitexCounter}")
            #print(f" - Uncommon words: {uncommonCounter}")
            print(f" - Words: {wordsDictCounter}")
            #print(f" - Common words percentage: {round((commonCounter/totalCounter)*100, 2)}%")
            #print(f" - Cenitex words percentage: {round((cenitexCounter/totalCounter)*100, 2)}%")
            #print(f" - Uncommon words percentage: {round((uncommonCounter/totalCounter)*100, 2)}%")
            print("----------------------------------------------")
            #pprint(sorted(uncommonWords,key=lambda i: i["counter"], reverse = True))
    printWords()
    print("Time: "+setElapsedTime(time.time() - start))
    #print("Please try printCommonWords(), printCenitexWords(), or printUncommonWords if you want to see any set of words.")
except Exception as e2:
    print(f" - Error: {str(e2)}")
