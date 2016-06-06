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

upoDict = csvToDict("../brikita-user-password-owner.csv") 

import hashlib
if upoDict[username][0] == hashlib.md5(password).hexdigest():
    templateRead = open("template.txt", "rU")
    template = templateRead.read()
    templateRead.close()
    
    outputHtml = template.replace("TITLE", "success")\
                         .replace("BODY", "<h1>Your login was successful</h1><a href='http://homer.stuy.edu/~nikita.borisov/BrikitaBrains.html'>Home</a>")
    print outputHtml
else:
    templateRead = open("template.txt", "rU")
    template = templateRead.read()
    templateRead.close()
    
    outputHtml = template.replace("TITLE", "error")\
                         .replace("BODY", "<h1>Your username or password is incorrect</h1><a href='http://homer.stuy.edu/~nikita.borisov/BrikitaLogin.html'>Back</a>")
    print outputHtml
