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
    return listOfLists

entry = eval(parseResults(results)[1][0].replace(";", ","))

htmlTemplate = '''
    <h1> Hi, USER. Here are your results: </h1>
    <h2> Average Times </h2>
    <p> Stage 1: TIME1 </p>
    <p> Stage 2: TIME2 </p>
    <p> Stage 3: TIME3 </p>
'''

import timecalculator
time1 = str(timecalculator.timeCalculator(entry[1], entry[10]))
time2 = str(timecalculator.timeCalculator(entry[11], entry[20]))
time3 = str(timecalculator.timeCalculator(entry[21], entry[30]))

htmlFinal = htmlTemplate.replace("TIME1", time1).replace("TIME2", time2).replace("TIME3", time3)
print htmlFinal    

# if isUser == True:
    # path = "~nikita.borisov/userDatabase" + user + ".csv"
    # resultsFile = open(path, "r")
    