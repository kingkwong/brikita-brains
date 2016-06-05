#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()
username = fromQS["username"].value
password = fromQS["password"].value
owner = fromQS["owner"].value
rpassword = fromQS["rpassword"].value

if rpassword == password:
    inputString = "\n" + username + "," + password + "," + owner 
    dest = open("../brikita-passwords.csv", "a", 0)
    dest.write(inputString)
    dest.close()
    
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
                         .replace("BODY", "<h1>Your two passwords don't match</h1><a href='http://homer.stuy.edu/~nikita.borisov/BrikitaSignUp.html'>Back</a>")
    print outputHtml