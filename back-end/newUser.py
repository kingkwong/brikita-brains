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

successHTMLTemplate = """
    <h1>Your sign up was successful</h1>
    <form method="POST" action="index.html">
        <input type="submit" value="Home"> 
    </form>
    <form action="user.py" method="POST">
        <input type="hidden" name="user" value="USER">
        <input type="submit" value="Show me the stuff">
    </form>
"""
existHTMLTemplate = '''
    <h1>Oh Noes!</h1>
    <p>It appears this username was already taken.</p>
    <p>Please either log into your existing account, or create a new one with an unclaimed username.</p>
    <form method="POST" action="BrikitaSignUp.html">
        <input type="submit" value="New User"> 
    </form>
    <form method="POST" action="BrikitaLogin.html">
        <input type="submit" value="Returning User"> 
    </form>
'''
badpassHTMLTemplate = '''
    <h1>Oh Noes!</h1>
    <p>Your two passwords don't match. Please try signing up again.</p>
    <form method="POST" action="BrikitaSignUp.html">
        <input type="submit" value="Try Again?"> 
    </form>
'''   
templateRead = open("template.txt", "rU")
template = templateRead.read()
templateRead.close()   
    
if rpassword == password:
    checkVacancy = csvToDict("/home/students/2018/nikita.borisov/brikita-user-password-owner.csv") 
    if username in checkVacancy:
        outputHtml = template.replace("TITLE", "Error | BrikitaBrains") \
                             .replace("BODY", existHTMLTemplate)
    else:
        import hashlib
        inputString = "\n" + username + "," + hashlib.sha256(password).hexdigest() + "," + owner 
        dest = open("/home/students/2018/nikita.borisov/brikita-user-password-owner.csv", "a", 0)
        dest.write(inputString)
        dest.close()
        
        outputHtml = template.replace("TITLE", "Success | BrikitaBrains") \
                             .replace("BODY", successHTMLTemplate.replace("USER", username))                        
else:   
    outputHtml = template.replace("TITLE", "Error | BrikitaBrains") \
                         .replace("BODY", badpassHTMLTemplate)
print outputHtml
