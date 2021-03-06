#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

# user authentication
try:
    user = fromQS["user"].value
    isUser = True
except:
    isUser = False
    
# RESET TEST FILE
# fix = open("/home/students/2018/nikita.borisov/userDatabase/n.csv", "w", 0)
# fixedContents = '''stroop,{1: '2016-06-09 14:04:51'; 2: '2016-06-09 14:04:56'; 3: '2016-06-09 14:04:59'; 4: '2016-06-09 14:05:00'; 5: '2016-06-09 14:05:03'; 6: '2016-06-09 14:05:05'; 7: '2016-06-09 14:05:07'; 8: '2016-06-09 14:05:09'; 9: '2016-06-09 14:05:10'; 10: '2016-06-09 14:05:12'; 11: '2016-06-09 14:05:14'; 12: '2016-06-09 14:05:16'; 13: '2016-06-09 14:05:19'; 14: '2016-06-09 14:05:29'; 15: '2016-06-09 14:05:58'; 16: '2016-06-09 14:05:59'; 17: '2016-06-09 14:06:00'; 18: '2016-06-09 14:06:03'; 19: '2016-06-09 14:06:04'; 20: '2016-06-09 14:06:05'; 21: '2016-06-09 14:06:06'; 22: '2016-06-09 14:06:06'; 23: '2016-06-09 14:06:07'; 24: '2016-06-09 14:06:08'; 25: '2016-06-09 14:06:08'; 26: '2016-06-09 14:06:09'; 27: '2016-06-09 14:06:09'; 28: '2016-06-09 14:06:11'; 29: '2016-06-09 14:06:13'; 30: '2016-06-09 14:06:15'; 31: '2016-06-09 14:06:18'},{'1': 9; '0': 1; '3': 10; '2': 8},{'2': 2; '1': 0; '3':0}'''
# fix.write(fixedContents)
# fix.close()

import resultsHelper

noResultsPage = '''
        <h1> Oh Noes! </h1>
        <p> It appeares you haven't played a game yet! To get your latest results, 
        please get started today! </p>
        <form action="games.py" method="POST">
            <input type="hidden" name="user" value="USER">
            <input type="submit" value="Let's play!">
        </form>
        <form action="user.py" method="POST">
            <input type="hidden" name="user" value="USER">
            <input type="submit" value="Back">
        </form>
    '''   
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
polyline = '''
    <h3> TITLE </h3>
    <svg height="500" width="1000">
        <rect height="500" width="1000" 
        style="stroke:black; stroke-width=2; fill:none"/>
        <polyline points="POINTS"
        style="stroke:blue; stroke-width=3; fill:none;"/>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="0" y="250">50</text>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="50" y="500">1st game</text>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="100" y="500">2nd game</text>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="150" y="500">3rd game</text>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="200" y="500">4th game</text>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="250" y="500">5th game</text>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="300" y="500">6th game</text>
        <text style="stroke:black; fill:black; stroke-width:1; font-size:12px;" x="350" y="500">7th game</text>
    </svg>
'''

# open and reads basic template file for html   
htmlTemplateFile = open("template.txt", "rU")
htmlTemplate = htmlTemplateFile.read()
htmlTemplateFile.close()

# checks if the user has a results file    
path = "/home/students/2018/nikita.borisov/userDatabase/" + user + ".csv"
try:
    csv = open(path, "rU")
except:
    isUser = "Fail"
    htmlBody = noResultsPage.replace("USER", user)
    finalHtml = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Error | BrikitaBrains")
    print finalHtml

# main code
if isUser == True:
    # reads user data from csv file
    results = csv.read()   
    csv.close() 
    
    # given times in the form of YYYY-MM-DD HH:MM:SS, calculate the difference between two times
    # in hours, minutes, and seconds
    import timecalculator
    listOfTime1 = []
    listOfTime2 = []
    listOfTime3 = []
    correctList = []
    # wrongList = []
    data = resultsHelper.parseResults(results)[1:]
    
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
    
    for dict in correctList:
        listOfCorrect1.append(str(dict["1"]*10) + "% correct")
        listOfCorrect2.append(str(dict["2"]*10) + "% correct")
        listOfCorrect3.append(str(dict["3"]*10) + "% correct")
    
    # generate results for user's overall performance
    timeOne   = timecalculator.timeDictToText(resultsHelper.averageTime(listOfTime1))
    timeTwo   = timecalculator.timeDictToText(resultsHelper.averageTime(listOfTime2))
    timeThree = timecalculator.timeDictToText(resultsHelper.averageTime(listOfTime3))
    
    accuracyOne   = str(int(resultsHelper.averageAcc(correctList, '1')*10)) + "% correct"
    accuracyTwo   = str(int(resultsHelper.averageAcc(correctList, '2')*10)) + "% correct"
    accuracyThree = str(int(resultsHelper.averageAcc(correctList, '3')*10)) + "% correct"
    
    finalSummary = summaryPage.replace("TIMEONE", timeOne) \
                              .replace("TIMETWO", timeTwo) \
                              .replace("TIMETHREE", timeThree) \
                              .replace("ACCURACYONE", accuracyOne) \
                              .replace("ACCURACYTWO", accuracyTwo) \
                              .replace("ACCURACYTHREE", accuracyThree)
    
    finalTime1 = []
    finalTime2 = []
    finalTime3 = []
    for timeDict in listOfTime1:
        finalTime1.append(timecalculator.timeDictToText(eval(timeDict)))
    for timeDict in listOfTime2:
        finalTime2.append(timecalculator.timeDictToText(eval(timeDict)))
    for timeDict in listOfTime3:
        finalTime3.append(timecalculator.timeDictToText(eval(timeDict)))
    
    # puts results into tables
    htmlBody = resultsHelper.tableGen(finalTime1, finalTime2, finalTime3, "Average Times") + \
               resultsHelper.tableGen(listOfCorrect1, listOfCorrect2, listOfCorrect3, "Average Accuracy") + \
               finalSummary + \
               links.replace("USER", user) + \
               polyline.replace("TITLE", "Times for trial 1")\
                       .replace("POINTS", resultsHelper.listToPolylinePoints(listOfTime1))+\
               polyline.replace("TITLE", "Times for trial 2")\
                       .replace("POINTS", resultsHelper.listToPolylinePoints(listOfTime2))+\
               polyline.replace("TITLE", "Times for trial 3")\
                       .replace("POINTS", resultsHelper.listToPolylinePoints(listOfTime3))+\
               polyline.replace("TITLE", "Accurcy for trial 1")\
                       .replace("POINTS", resultsHelper.listToPolylinePoints(listOfCorrect1))+\
               polyline.replace("TITLE", "Accurcy for trial 2")\
                       .replace("POINTS", resultsHelper.listToPolylinePoints(listOfCorrect2))+\
               polyline.replace("TITLE", "Accurcy for trial 3")\
                       .replace("POINTS", resultsHelper.listToPolylinePoints(listOfCorrect3))

    
    # sets up final html page to return
    htmlFinal = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Results | BrikitaBrains")
    print htmlFinal
    
elif isUser == False:
    # user failed to authenticate; redirect user
    file = open("lost.html", "rU")
    print file.read()
    file.close()