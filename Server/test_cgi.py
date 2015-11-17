#!/usr/bin/python
import cgi

print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hello World!</p>"
print "<p>I'm testing!</p>"

arguments = cgi.FieldStorage()

print("here's cgi params ")
for key in arguments.keys():
        print(key)
        if key == '@frames':
                print("enter frames_1")
                fw = open("/Users/zlfengyi/http_test.pcm", "wb")
                print("enter frames_2")
                fw.write(arguments[key].value)
                fw.close()
                print("receive frames successfully.")
        else:
                print(key + " " + arguments[key].value)
                
