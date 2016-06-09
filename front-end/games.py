#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()

htmlTemplate = '''
	<!DOCTYPE html>
	<html>
	<head>
		<title>Games</title>
	</head>
	<body>
		<h1> Here are some of our current game options: </h1>
		<form method="POST" action="stroop.py">
			<input type="hidden" name="user" value="USER">
			<input type="hidden" name="level" value="1">
			<input type="hidden" name="numright" value="0">
			<input type="hidden" name="numwrong" value="0">
            <input type="hidden" name="timeDict" value="{}">
			<input type="submit" value="Stroop Test">
		</form>
	</body>
	</html>
'''

# user authentication setup
try:
	user = fromQS["user"].value
	outputHtml = htmlTemplate.replace("USER", user)
	print outputHtml
except:
	print '''
		<h1> Lost? </h1>
		<p> It appears you have not login yet. Here are some helpful links: </p>
		<a href="http://homer.stuy.edu/~nikita.borisov/project/BrikitaLogin.html"> <button>Login</button></a> <br>
		<a href="http://homer.stuy.edu/~nikita.borisov/project/BrikitaSignUp.html"> <button>Sign Up!</button></a> <br>
		<a href="http://homer.stuy.edu/~nikita.borisov/project/BrikitaBrains.html"> <button>Homepage</button></a> <br>
	'''


