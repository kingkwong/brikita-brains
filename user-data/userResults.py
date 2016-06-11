#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

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

def parseResults (contents):
    listOfTrials = contents.split("\n")
    listOfLists = []
    for trial in listOfTrials:
        sublist = trial.split(",")[1:]
        listOfLists.append(sublist)
    return listOfLists
    
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
   
htmlTemplateFile = open("template.txt", "rU")
htmlTemplate = htmlTemplateFile.read()
htmlTemplateFile.close()
    
path = "/home/students/2018/nikita.borisov/userDatabase/" + user + ".csv"
try:
    csv = open(path, "rU")
except:
    isUser = "Fail"
    htmlBody = noResultsPage.replace("USER", user)
    finalHtml = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Error | BrikitaBrains")
    print finalHtml

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
    data = parseResults(results)[1:]
    
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

    listOfCorrect1 = []
    listOfCorrect2 = []
    listOfCorrect3 = []
    
    for dict in correctList:
        listOfCorrect1.append(str(dict["1"]*10) + "% correct")
        listOfCorrect2.append(str(dict["2"]*10) + "% correct")
        listOfCorrect3.append(str(dict["3"]*10) + "% correct")
        
    htmlBody = tableGen(listOfTime1, listOfTime2, listOfTime3, "Average Times") + \
               tableGen(listOfCorrect1, listOfCorrect2, listOfCorrect3, "Average Accuracy") + \
               links.replace("USER", user)
    
    htmlFinal = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Results | BrikitaBrains")
    print htmlFinal
elif isUser == False:
    file = open("lost.html", "rU")
    print file.read()
    file.close()
    