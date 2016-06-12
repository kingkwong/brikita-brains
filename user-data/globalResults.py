#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

    
# RESET TEST FILE
# fix = open("/home/students/2018/nikita.borisov/userDatabase/n.csv", "w", 0)
# fixedContents = '''stroop,{1: '2016-06-09 14:04:51'; 2: '2016-06-09 14:04:56'; 3: '2016-06-09 14:04:59'; 4: '2016-06-09 14:05:00'; 5: '2016-06-09 14:05:03'; 6: '2016-06-09 14:05:05'; 7: '2016-06-09 14:05:07'; 8: '2016-06-09 14:05:09'; 9: '2016-06-09 14:05:10'; 10: '2016-06-09 14:05:12'; 11: '2016-06-09 14:05:14'; 12: '2016-06-09 14:05:16'; 13: '2016-06-09 14:05:19'; 14: '2016-06-09 14:05:29'; 15: '2016-06-09 14:05:58'; 16: '2016-06-09 14:05:59'; 17: '2016-06-09 14:06:00'; 18: '2016-06-09 14:06:03'; 19: '2016-06-09 14:06:04'; 20: '2016-06-09 14:06:05'; 21: '2016-06-09 14:06:06'; 22: '2016-06-09 14:06:06'; 23: '2016-06-09 14:06:07'; 24: '2016-06-09 14:06:08'; 25: '2016-06-09 14:06:08'; 26: '2016-06-09 14:06:09'; 27: '2016-06-09 14:06:09'; 28: '2016-06-09 14:06:11'; 29: '2016-06-09 14:06:13'; 30: '2016-06-09 14:06:15'; 31: '2016-06-09 14:06:18'},{'1': 9; '0': 1; '3': 10; '2': 8},{'2': 2; '1': 0; '3':0}'''
# fix.write(fixedContents)
# fix.close()

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

def parseResults (contents):
    listOfTrials = contents.split("\n")
    listOfLists = []
    for trial in listOfTrials:
        sublist = trial.split(",")[1:]
        listOfLists.append(sublist)
    return listOfLists
    
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

links = '''
    <form action="BrikitaBrains.html" method="POST">
        <input type="submit" value="Back">
    </form> 
'''
summaryPage = '''
    <br>
    <h1> Overall Times </h1>
        <h2> Test 1: TIMEONE </h2>
        <h2> Test 2: TIMETWO </h2>
        <h2> Test 3: TIMETHREE </h2>
    <br>
    <h1> Overall Accuracy <h1>
        <h2> Test 1: ACCURACYONE </h2>
        <h2> Test 2: ACCURACYTWO </h2>
        <h2> Test 3: ACCURACYTHREE </h2>
    <br>
'''

# open and reads basic template file for html   
htmlTemplateFile = open("template.txt", "rU")
htmlTemplate = htmlTemplateFile.read()
htmlTemplateFile.close()

# finding all the result files  
userListings = csvToDict("/home/students/2018/nikita.borisov/brikita-user-password-owner.csv") 
results = {}
time1Records = []
time2Records = []
time3Records = []
acc1Records = []
acc2Records = []
acc3Records = []
for i in userListings:
    path = "/home/students/2018/nikita.borisov/userDatabase/" + i + ".csv"
    try:
        csv = open(path, "rU")
        results[i] = csv.read()   
        csv.close() 
        # given times in the form of YYYY-MM-DD HH:MM:SS, calculate the difference between two times
        # in hours, minutes, and seconds
        import timecalculator
        listOfTime1 = []
        listOfTime2 = []
        listOfTime3 = []
        correctList = []
        data = parseResults(results[i])[1:]    
        # parses data to get list of times for each trial
        for entry in data:
            # print entry
            # calculations for average time of each trial
            time = eval(entry[0].replace(";", ","))
            time1 = str(timecalculator.timeCalculator(time[1], time[10]))
            time2 = str(timecalculator.timeCalculator(time[11], time[20]))
            time3 = str(timecalculator.timeCalculator(time[21], time[30]))
            listOfTime1.append(time1)
            listOfTime2.append(time2)
            listOfTime3.append(time3)
            # calculations for numright/numwrong
            correct = eval(entry[1].replace(";", ","))
            # wrong = eval(entry[2].replace(";", ","))
            correctList.append(correct)
            # wrongList.append(wrong)
        # print correctList, wrongList
        # creates a list of how accurate the user was in each of the three trials
        listOfCorrect1 = []
        listOfCorrect2 = []
        listOfCorrect3 = []   
        # generate results for user's overall performance
        time1Records.append(i + ":" + str(minTime(listOfTime1)))
        time2Records.append(i + ":" + str(minTime(listOfTime2)))
        time3Records.append(i + ":" + str(minTime(listOfTime3)))
        acc1Records.append(i + ":" + str(int(maxAcc(correctList, '1')*10)) + "% correct")
        acc2Records.append(i + ":" + str(int(maxAcc(correctList, '2')*10)) + "% correct")
        acc3Records.append(i + ":" + str(int(maxAcc(correctList, '3')*10)) + "% correct") 
    except:
        pass
# puts results into tables
htmlBody = tableGen(time1Records, time2Records, time3Records, "Min Times") + tableGen(acc1Records, acc2Records, acc3Records, "Max Accuracy") + links 
# sets up final html page to return
htmlFinal = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Results | BrikitaBrains")
print htmlFinal
