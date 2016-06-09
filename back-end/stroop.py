#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()
level = int(fromQS["level"].value)
numright = fromQS["numright"].value
numwrong = fromQS["numwrong"].value
timeDict = eval(fromQS["timeDict"].value)
user = fromQS["user"].value

from datetime import datetime
timeDict[level] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if level != 1:
	oldAnswer = fromQS["oldanswer"].value
	userAnswer = fromQS["useranswer"].value
	if oldAnswer == userAnswer:
		numright = str(int(numright)+1)
	else:
		numwrong = str(int(numwrong)+1)
	
import random
stage = 0
listOfColors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
nextWord = random.choice(listOfColors)
nextColor = nextWord

if level <= 10:
	nextColor = "black"
	stage = 1
elif level <= 20:
	stage = 2
elif level <= 30:
	while nextColor == nextWord:
		nextColor = random.choice(listOfColors)
	stage = 3	

question = str(level)
level = str(level+1)

stroopTemplate = """
<h2> You are currently on question QUESTION </h2>
<p> INSTRUCTIONS </p>
<svg>
 <text x="20" y="40" style="fill: COLOR; stroke: COLOR; font-size: 48px;"> WORD </text>
</svg>
<form method="POST" action="stroop.py">
	<!-- hidden variables -->
	<input type="hidden" name="level" value="LVL">
	<input type="hidden" name="user" value="USER">
	<input type="hidden" name="oldanswer" value="OLDANSWER">
	<input type="hidden" name="numright" value="NUMRIGHT">
	<input type="hidden" name="numwrong" value="NUMWRONG">
    <input type="hidden" name="timeDict" value="TIMEDICT">
	<!-- static part begins-->
	<input type="radio" name="useranswer" value="red"> RED <br>
	<input type="radio" name="useranswer" value="blue"> BLUE <br>
	<input type="radio" name="useranswer" value="green"> GREEN <br>
	<input type="radio" name="useranswer" value="yellow"> YELLOW <br>
	<input type="radio" name="useranswer" value="orange"> ORANGE <br>
	<input type="radio" name="useranswer" value="purple"> PURPLE <br>
	<input type="radio" name="useranswer" value="pink"> PINK <br>
	<input type="submit" value="SUBMIT">
	<!-- static part ends -->
</form>
<p> Correct: NUMRIGHT </p>
<p> Incorrect: NUMWRONG </p>
"""

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
   
if stage != 0:
    instructions = returnInstructions(stage)
    print stroopTemplate.replace("COLOR", nextColor) \
        .replace("WORD", nextWord) \
        .replace("LVL", level) \
        .replace("INSTRUCTIONS", instructions) \
        .replace("NUMRIGHT", numright) \
        .replace("NUMWRONG", numwrong) \
        .replace("OLDANSWER", nextWord) \
        .replace("QUESTION", question)\
        .replace("USER", user)\
        .replace("TIMEDICT", str(timeDict))
else:
    print """
        Test Done
        """
    resultCsvLine = "\n" + "stroop" + "," + str(timeDict) + "," + numright + "," + numwrong
    path = "../../userDatabase/" + user + ".csv"
    dest = open(path, "a" , 0)
    dest.write(resultCsvLine)
    dest.close()
    


