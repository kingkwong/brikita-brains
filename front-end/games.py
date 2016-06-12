#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

# user authentication setup
try:
    user = fromQS["user"].value
    isUser = True
except:
    isUser = False

htmlBodyTemplate = '''
		<h1> Here are some of our current game option(s): </h1>
		<form method="POST" action="stroopSetup.py">
            <!-- setup variables -->
			<input type="hidden" name="user" value="USER">
			<input type="submit" value="Stroop Test">
		</form>
        <form action="user.py" method="POST">
            <input type="hidden" name="user" value="USER">
            <input type="submit" value="Back">
        </form> 
    '''

if isUser == True:
    htmlTemplateFile = open("template.txt", "rU")
    htmlTemplate = htmlTemplateFile.read()
    htmlTemplateFile.close()
    htmlBody = htmlBodyTemplate.replace("USER", user)
    htmlFinal = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", "Games | BrikitaBrains")
    print htmlFinal
else:
    file = open("lost.html", "rU")
    print file.read()
    file.close()
