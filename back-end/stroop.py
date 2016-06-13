#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

# import various values from query string
level = int(fromQS["level"].value)
numright = fromQS["numright"].value
numwrong = fromQS["numwrong"].value
timeDict = eval(fromQS["timeDict"].value)
numRightDict = eval(fromQS["numRightDict"].value)
numWrongDict = eval(fromQS["numWrongDict"].value)
user = fromQS["user"].value

# records time
from datetime import datetime
timeDict[level] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

import random
stage =0
outline="white"
listOfColors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
nextWord = random.choice(listOfColors)
nextColor = nextWord
question = str(level)

# sets stage
if level <= 10:
    nextColor = "black"
    stage = 1
    outline="white"
elif level <= 20:
    stage = 2
    outline="black"
elif level <= 30:
    outline="black"
    while nextColor == nextWord:
        nextColor = random.choice(listOfColors)
    stage = 3

# checks if answer is right or wrong, then adds it to counter
if level != 1:
    oldAnswer = fromQS["oldanswer"].value
    userAnswer = fromQS["useranswer"].value
    if oldAnswer == userAnswer:
        numright = str(int(numright)+1)
        try:
            numRightDict[str(stage)] += 1
        except:
            numRightDict[str(stage)] = 1
    else:
        numwrong = str(int(numwrong)+1)
        try:
            numWrongDict[str(stage)] += 1         
        except:
            numWrongDict[str(stage)] = 1

level = str(level+1)
# print stage

stroopHtmlFile = open("stroopTemplate.html", "rU")
stroopTemplate = stroopHtmlFile.read()
stroopHtmlFile.close()

def returnInstructions (stage):
        if stage == 1:
                return '''
                        The following words will be in BLACK ink. For example, the word "RED" will
                        be in the color BLACK. Choose the option that corresponds to what the word says.
                        In this example, it would be the option RED.
                '''
        if stage == 2:
                return '''
                        The following words will be in various colors. The ink that the word is in will
                        match the word. For example, the word "RED" will be in the color RED. Choose the
                        option that corresponds to what the word says. In this example, it would be the
                        option RED.
                '''
        if stage == 3:
                return '''
                        The following words will be in various colors. The ink that the word is in will
                        NOT match the word. For example, the word "RED" could be in the color BLUE. Choose the
                        option that corresponds to what the word says, regardless of what ink it is in. In this
                        example, it would be the option RED.
               '''

htmlDone = '''
    <h1> Thank you for your assistance. </h1>
    <p> Here are some useful links to check out: </p>
	<a href="http://homer.stuy.edu/~nikita.borisov/project/BrikitaBrains.html"> <button>Homepage</button></a> <br>
    <form action="userResults.py" method="POST">
        <input type="hidden" name="user" value="USER">
        <input type="submit" value="RESULTS">
    </form>
'''
if stage != 0:
    instructions = returnInstructions(stage)
    # print stage
    print stroopTemplate.replace("COLOR", nextColor) \
        .replace("WORD", nextWord) \
        .replace("LVL", level) \
        .replace("INSTRUCTIONS", instructions) \
        .replace("NUMRIGHTDICT", str(numRightDict)) \
        .replace("NUMWRONGDICT", str(numWrongDict)) \
        .replace("NUMRIGHT", numright) \
        .replace("NUMWRONG", numwrong) \
        .replace("OLDANSWER", str(nextWord)) \
        .replace("QUESTION", question)\
        .replace("USER", user)\
        .replace("TIMEDICT", str(timeDict))\
        .replace("OUTLINE", outline)
else:
    htmlTemplateFile = open("template.txt", "rU")
    htmlTemplate = htmlTemplateFile.read()
    htmlTemplateFile.close()
    htmlDone = htmlDone.replace("USER", user)
    htmlFinal = htmlTemplate.replace("BODY", htmlDone).replace("TITLE", "Stroop | BrikitaBrains")
    print htmlFinal
    times = str(timeDict).replace(",", ";")
    numRights = str(numRightDict).replace(",", ";")
    numWrongs = str(numWrongDict).replace(",", ";")
    resultCsvLine = "\n" + "stroop" + "," + times + "," + numRights + "," + numWrongs
    path = "/home/students/2018/nikita.borisov/userDatabase/" + user + ".csv"
    dest = open(path, "a", 0)
    dest.write(resultCsvLine)
    dest.close()