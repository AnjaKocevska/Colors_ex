#!/usr/local/bin/python3

import cgi
import cgitb
cgitb.enable()

data=cgi.FieldStorage()
name= data.getvalue("name")
color=data.getvalue("color")

f= open("/Users/anjakocevska/Desktop/dadada/cgi-bin/colorlist.txt","r")
reading = f.read()

print("""
<p></p>
    """)

if color in reading:
    print("""
    <h1 style="color: {}">Hi {}, {} Is a color</h1>""" .format(color,name,color))
else:
    print("""
    <h1>Yo %s, %s Is not a color</h1>""" %(name,color))