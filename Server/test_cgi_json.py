#!/usr/bin/python
import cgi
import json
from base64 import b64encode

print "Content-type: application/json"

'''print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hello World!</p>"
print "<p>I'm testing!</p>"
'''

args = cgi.FieldStorage()
if ("@index" in args.keys() and "@lpcm" in args.keys()):
	print "receive params successfully"
	pa = "/home/zlfengyi/breeze/Server/asr/bin/wav/"
	name = pa + args["@index"].value + ".lpcm"
	open(name, "wb").write(args["@lpcm"].value)
	open(name+"_done", "wb").write("Hello C!")
	
	print json.dumps({"@lpcm":b64encode(args["@lpcm"].value)
		})
	#print "write to file successfully"
	#print 	
	
	# return json respose"
	'''
	data = {}
	data["test_num"] = 0
	name = 
	while 1>0 :
		if (os.path.exists())
	print os.path
	'''
#print json.dumps({'Cost':'99'})