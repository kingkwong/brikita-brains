#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

htmlTemplate = '''
<h1> Hello, USER. </h1>
<p> Here are just a few things you can do: </p>
<form action="games.py" method="POST">
    <input type="hidden" name="user" value="USER">
    <input type="submit" value="GAMES">
</form>
<form action="userResults.py" method="POST">
    <input type="hidden" name="user" value="USER">
    <input type="submit" value="RESULTS">
</form>
'''

try:
    user = fromQS["user"].value
    htmlFinal = htmlTemplate.replace("USER", user)
    print htmlFinal
except:
    file = open("lost.html", "r")
    print file.read()
    file.close()