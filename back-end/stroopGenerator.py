#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import cgi
fromQS = cgi.FieldStorage()
nextColor = fromQS["nextColor"].value
nextWord = fromQS["nextWord"].value

stroopTemplate = """
<svg>
 <text x="20" y="40" style="fill: COLOR; stroke: COLOR; font-size: 48px;"> WORD </text>
</svg>
"""

outputHtml = stroopTemplate.replace("COLOR", nextColor)\
                           .replace("WORD", nextWord)

print outputHtml


