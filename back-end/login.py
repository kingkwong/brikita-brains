#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

def csvToDict(filename):
    fo = open(filename, "rU")
    csv = fo.read()
    fo.close()
    listOfLines = csv.split("\n")
    output = {}
    for line in listOfLines:
        listOfValues = line.split(",")
        output[listOfValues[0]] = listOfValues[1:]
    return output

import cgi
fromQS = cgi.FieldStorage()
username = fromQS["username"].value
password = fromQS["password"].value

upoDict = csvToDict("/home/students/2018/nikita.borisov/brikita-user-password-owner.csv") 

templateRead = open("template.txt", "rU")
template = templateRead.read()
templateRead.close()

successHTMLTemplate = """
    <h1>Your login was successful</h1>
    <form action="index.html" method="POST">
        <input type="submit" value="Home">
    </form>
    <form action="user.py" method="POST">
        <input type="hidden" name="user" value="USER">
        <input type="submit" value="Show me the stuff!">
    </form>
"""

badLoginHTMLTemplate = '''
    <h1>Your username or password is incorrect</h1>
    <form action="BrikitaLogin.html" method="POST">
        <input type="hidden" name="user" value="USER">
        <input type="submit" value="Try Again?">
    </form>
'''

import hashlib
try:
    if upoDict[username][0] == hashlib.sha256(password).hexdigest():      
        outputHtml = template.replace("TITLE", "Success | BrikitaBrains")\
                             .replace("BODY", successHTMLTemplate.replace("USER", username))
    else:
        outputHtml = template.replace("TITLE", "Error | BrikitaBrains")\
                             .replace("BODY", badLoginHTMLTemplate)
except:
    outputHtml = template.replace("TITLE", "Error | BrikitaBrains")\
                         .replace("BODY", badLoginHTMLTemplate)
print outputHtml
