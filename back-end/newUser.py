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


if rpassword == password:
    checkVacancy = csvToDict("../../brikita-user-password-owner.csv") 
    if username in checkVacancy:
        templateRead = open("template.txt", "rU")
        template = templateRead.read()
        templateRead.close()
    
        outputHtml = template.replace("TITLE", "error")\
                             .replace("BODY", "<h1>This username already exists</h1><a href='http://homer.stuy.edu/~nikita.borisov/project/BrikitaSignUp.html'>Back</a>")
        print outputHtml
    else:
        import hashlib
        inputString = "\n" + username + "," + hashlib.md5(password).hexdigest() + "," + owner 
        dest = open("../../brikita-user-password-owner.csv", "a", 0)
        dest.write(inputString)
        dest.close()
    
        templateRead = open("template.txt", "rU")
        template = templateRead.read()
        templateRead.close()
    
        outputHtml = template.replace("TITLE", "success")\
                             .replace("BODY", "<h1>Your sign up was successful</h1><a href='http://homer.stuy.edu/~nikita.borisov/project/BrikitaBrains.html'>Home</a>")
        print outputHtml                         
else:
    templateRead = open("template.txt", "rU")
    template = templateRead.read()
    templateRead.close()
    
    outputHtml = template.replace("TITLE", "error")\
                         .replace("BODY", "<h1>Your two passwords don't match</h1><a href='http://homer.stuy.edu/~nikita.borisov/project/BrikitaSignUp.html'>Back</a>")
    print outputHtml
