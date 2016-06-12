#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

# user authenticate code
try:
    user = fromQS["user"].value
    isUser = True
except:
    isUser = False

htmlTemplateBody = '''
    <h1> Hello, USER. </h1>
    <p> Here are just a few things you can do: </p>
    <form action="games.py" method="POST">
        <input type="hidden" name="user" value="USER">
        <input type="submit" value="Games">
    </form>
    <form action="userResults.py" method="POST">
        <input type="hidden" name="user" value="USER">
        <input type="submit" value="My Results">
    </form>
    <form action="globalResults.py" method="POST">
        <input type="hidden" name="user" value="USER">
        <input type="submit" value="Leaderboard">
    </form>
        <form action="index.html" method="POST">
        <input type="submit" value="Homepage">
    </form>
'''

if isUser == True:
    htmlTemplateFile = open("template.txt", "rU")
    htmlTemplate = htmlTemplateFile.read()
    htmlTemplateFile.close()
    htmlBody = htmlTemplateBody.replace("USER", user)
    htmlFinal = htmlTemplate.replace("BODY", htmlBody).replace("TITLE", user + " | BrikitaBrains")
    print htmlFinal
else:
    file = open("lost.html", "rU")
    print file.read()
    file.close()