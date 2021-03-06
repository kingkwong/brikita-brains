#! /usr/bin/python



print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

# user authenticate code
try:
    user = fromQS["user"].value
    isUser = True
except:
    isUser = False

import resultsHelper

links = '''
    <form action="user.py" method="POST">
        <input type="hidden" name="user" value="USER">
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
def sortByValues(dict, direction):
    if direction == 0:
        output = []
        i = 0 
        while i < len(dict.values()):
            for j in dict:
                if dict[j] == sorted(dict.values())[i]:
                    output.append(j + ":" + str(sorted(dict.values())[i]) + " seconds")
                    toPOP = j
            dict.pop(toPOP)
            i += 1
    else:
        output = []
        i = 0 
        while i < len(dict.values()):
            for j in dict:
                if dict[j] == sorted(dict.values()[::-1])[i]:
                    output.append(j + ":" + str(sorted(dict.values()[::-1])[i]) + "%")
                    toPOP = j
            dict.pop(toPOP)
            i += 1
    return list(set(output))
# open and reads basic template file for html   
htmlTemplateFile = open("template.txt", "rU")
htmlTemplate = htmlTemplateFile.read()
htmlTemplateFile.close()

# finding all the result files  
userListings = resultsHelper.csvToDict("/home/students/2018/nikita.borisov/brikita-user-password-owner.csv") 
results = {}
time1Records = {}
time2Records = {}
time3Records = {}
acc1Records = {}
acc2Records = {}
acc3Records = {}
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
        data = resultsHelper.parseResults(results[i])[1:] 
        
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
        time1Records[i] = int(timecalculator.timeDictToText(resultsHelper.minTime(listOfTime1)).replace(" seconds", ""))
        time2Records[i] = int(timecalculator.timeDictToText(resultsHelper.minTime(listOfTime2)).replace(" seconds", ""))
        time3Records[i] = int(timecalculator.timeDictToText(resultsHelper.minTime(listOfTime3)).replace(" seconds", ""))
        acc1Records[i] = resultsHelper.maxAcc(correctList, '1')*10
        acc2Records[i] = resultsHelper.maxAcc(correctList, '2')*10
        acc3Records[i] = resultsHelper.maxAcc(correctList, '3')*10

        
    except:
        pass

if isUser == True:        
    # puts results into tables
    htmlBody = resultsHelper.tableGen(sortByValues(time1Records, 0), sortByValues(time2Records, 0), sortByValues(time3Records, 0), "Min Times") + \
               resultsHelper.tableGen(sortByValues(acc1Records, 1), sortByValues(acc2Records, 1), sortByValues(acc3Records, 1), "Max Accuracy") + \
               links.replace("USER", user)
               
    # sets up final html page to return
    htmlFinal = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Results | BrikitaBrains")

    print htmlFinal
else:
    file = open("lost.html", "rU")
    print file.read()
    file.close()