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
    
if isUser == True:
    htmlBody = '''
        <h1> Welcome to Stroop Paints Co. </h1>
        <p> Congratulations! You have been chosen out of hundreds of applicants for this position. </p>
        <p> 
            Your task is simple. You are the crane operator. On the control panel,
            there are a number of buttons. One is the color selector. Our assembly
            line churns out colored paint cans. Each paint can is labeled with a word.
        </p>
        <p> The first 10 paint cans will be colored black. The next ten have labels that
        match the color of the word. For example, a RED can with the label "RED" on it.
        Due to a paint spillage at one of the factories, the last 10 will have labels that won't
        match the color of the word. In all three cases, please select the word stated on the label,
        regardless of what color the can has been painted. Lock in your selection
            with the button directly under the selector.
        <p>
            I must warn you, the cans will only be displayed for about FIVE seconds, after
            which, the can and its label are no longer visible. You have our full confidence.
            Don't let us down.
        </p>
        <form method="POST" action="stroop.py">
            <!-- setup variables -->
			<input type="hidden" name="user" value="USER">
			<input type="hidden" name="level" value="1">
			<input type="hidden" name="numright" value="0">
			<input type="hidden" name="numwrong" value="0">
            <input type="hidden" name="timeDict" value="{}">
            <input type="hidden" name="numRightDict" value="{}">
            <input type="hidden" name="numWrongDict" value="{}">
			<input type="submit" value="I'm on it, sir.">
		</form>
    '''
    htmlTemplateFile = open("template.txt", "rU")
    htmlTemplate = htmlTemplateFile.read()
    htmlTemplateFile.close()
    htmlBody = htmlBody.replace("USER", user)
    htmlFinal = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Stroop | BrikitaBrains")
    print htmlFinal
else:
    file = open("lost.html", "rU")
    print file.read()
    file.close()