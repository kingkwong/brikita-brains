# finds the maximum accuracy for a user
def maxAcc (listOfDict, key):
    list = []
    for dict in listOfDict:
        list.append(dict[key])
    maximum = max(list)
    return maximum

# finds the minimum time for a user
def minTime (listOfDict):
    listOfHours = []
    listOfMinutes = []
    listOfSeconds = []
    for dict in listOfDict:
        dict = eval(dict)
        listOfHours.append(dict["hours"])
        listOfMinutes.append(dict["minutes"])
        listOfSeconds.append(dict["seconds"])
    minHour = min(listOfHours)
    minMinute = min(listOfMinutes)
    minSecond = min(listOfSeconds)
    minDict = {
        "hours"   : minHour,
        "minutes" : minMinute,
        "seconds" : minSecond,
    }
    return minDict

# converts a file into a list of data that can be iterated through
def parseResults (contents):
    listOfTrials = contents.split("\n")
    listOfLists = []
    for trial in listOfTrials:
        sublist = trial.split(",")[1:]
        listOfLists.append(sublist)
    return listOfLists

# converts a csv file into a dictionary    
def csvToDict(filename):
    fo = open(filename, "rU")
    csv = fo.read()
    fo.close()
    listOfLines = csv.split("\n")
    output = {}
    for line in listOfLines:
        listOfValues = line.split(",")
        output[listOfValues[0]] = listOfValues[1:]
    return output

# makes a table out of the elements in each of the three input lists    
def tableGen (list1, list2, list3, caption):
    tableTemplate = '''
        <table>
            <caption> <h1> CAPTION </h1> </caption>
            <tbody>
                <tr>
                    <th> Test 1 </th>
                    <th> Test 2 </th>
                    <th> Test 3 </th>
                </tr>
                TABLECONTENTS
            </tbody>
        </table>
    '''
    i = 0
    finalEntry = ""
    while i < len(list1):
        subentry1 = "<td>" + str(list1[i]) + "</td>"
        subentry2 = "<td>" + str(list2[i]) + "</td>"
        subentry3 = "<td>" + str(list3[i]) + "</td>"
        entry = "<tr>" + subentry1 + subentry2 + subentry3 + "</tr>\n"
        finalEntry += entry
        i += 1
    finalTable = tableTemplate.replace("TABLECONTENTS", finalEntry).replace("CAPTION", caption)
    return finalTable

# converts a list into a plottable graph    
def listToPolylinePoints(list):
    outputList = []
    i = 0
    while i < len(list):
        outputList.append((i+1)*50)
        try:
            outputList.append(500-5*int(eval(list[i])["seconds"]))
        except:
            outputList.append(500-5*int(list[i].replace("% correct", "")))
        i += 1
    outputStr = ""
    j = 0
    while j < len(outputList):
        outputStr += str(outputList[j]) + "," + str(outputList[j+1]) + " "
        j += 2
    return outputStr
    
def averageAcc (listOfDict, key):
    list = []
    for dict in listOfDict:
        list.append(dict[key])
    length = float(len(list))
    average = sum(list)/length
    return average

# finds the average time of a list of dictionaries with the keys "hours", "minutes", "seconds"    
def averageTime (listOfDict):
    length = len(listOfDict)
    listOfHours = []
    listOfMinutes = []
    listOfSeconds = []
    for dict in listOfDict:
        dict = eval(dict)
        listOfHours.append(dict["hours"])
        listOfMinutes.append(dict["minutes"])
        listOfSeconds.append(dict["seconds"])
    averageHour = sum(listOfHours)/length
    averageMinute = sum(listOfMinutes)/length
    averageSecond = sum(listOfSeconds)/length
    averageDict = {
        "hours"   : averageHour,
        "minutes" : averageMinute,
        "seconds" : averageSecond,
    }
    return averageDict