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

upoDict = csvToDict("../Documents/user-pass.txt") 

if upoDict[username][0] == password:
    fo = open("../Documents/hiddenData.txt", "rU")
    data = fo.read()
    fo.close()
    print "Hello " + upoDict[username][1] + "<br>" + data
else:
    print "sorry your username or password isn't correct"
