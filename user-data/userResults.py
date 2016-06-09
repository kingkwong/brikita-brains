#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

# RESULTS PAGE
# try:
	# user = fromQS["user"].value
    # isUser = True
# except:
    # isUser = False
    
csv = open("/home/students/2018/nikita.borisov/userDatabase/bk.csv", "r")
results = csv.read()

def parseResults (contents):
    listOfTrials = contents.split("\n")
    listOfLists = []
    for trial in listOfTrials:
        sublist = trial.split(",")[1:]
        listOfLists.append(sublist)
    return listOfLists[1:]

import timecalculator
listOfTime1 = []
listOfTime2 = []
listOfTime3 = []
data = parseResults(results)[1:]

for entry in data:
    time = eval(entry[0].replace(";", ","))
    time1 = str(timecalculator.timeCalculator(time[1], time[10]))
    time2 = str(timecalculator.timeCalculator(time[11], time[20]))
    time3 = str(timecalculator.timeCalculator(time[21], time[30]))
    listOfTime1.append(time1)
    listOfTime2.append(time2)
    listOfTime3.append(time3)
    
def tableGen (list1, list2, list3):
    tableTemplate = '''
        <table border="1">
            <caption> </caption>
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
    finalTable = tableTemplate.replace("TABLECONTENTS", finalEntry)
    return finalTable

htmlFinal = tableGen(listOfTime1, listOfTime2, listOfTime3)
print htmlFinal    

# if isUser == True:
    # path = "~nikita.borisov/userDatabase" + user + ".csv"
    # resultsFile = open(path, "r")
    