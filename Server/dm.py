#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import json
import time
import os
import subprocess
import xml.etree.ElementTree as ET
from base64 import b64encode

def getTTS(text):
	command = 'cd tts/bin\n export LD_LIBRARY_PATH=../lib\n ./ttsdemo \"' + text + '\" '
	command2 = './ttsdemo \"%s\" > tmp.txt'%text
	os.putenv('LD_LIBRARY_PATH', '/home/zlfengyi/breeze/Server/tts/lib')
	os.system(command2)
#	devnull = open('/dev/null', 'w')
	#p = subprocess.Popen(command, shell=True)
	#p.wait()
#	subprocess.call(command)
	return open('tts/bin/tts.lpcm', 'rb').read() 
def work(root, res):
	for x in root.iter("action"):
		if x.get("id") == "12001":
			res["rgb"] = [200, 200, 200]
			res["tts"] = "light_1.wav" # 好的，开灯 
		elif x.get("id") == "12002":
			res["rgb"] = [0, 0, 0]
			res["tts"] = "light_2.wav" # 好的，关灯 
		elif x.get("id") == "12003": # make it darker
			if sum(res["rgb"]) > 0:
				for i in xrange(3):
					res["rgb"][i] /= 2
				res["tts"] = "light_3.wav"
			else:
				res["tts"] = "light_9.wav" #TODO: change to light_10.wav
			
	for x in root.iter("color"):
		if x.get("id") == "13001":
			res["rgb"] = [200, 0, 0]
		elif x.get("id") == "13003":
			res["rgb"] = [0, 0, 200]
		elif x.get("id") == "13004":
			res["rgb"] = [141, 75, 187]

print "Content-type: application/json"
print # this line ends the hearder, and start to print body

args = cgi.FieldStorage()
result = json.loads(args["@state"].value)
if ("@index" in args.keys() and "@lpcm" in args.keys()):
	pa = "/home/zlfengyi/breeze/Server/asr/bin/wav/"
	name = pa + args["@index"].value + ".lpcm"
	open(name, "wb").write(args["@lpcm"].value)
	open(name+"_done", "wb").write("Hello C!")

	# result["@debug"] = "Server write lpcm successfully"
	#print json.dumps({"@lpcm":b64encode(args["@lpcm"].value)
	#	})
	
	# return json respose after asr executing"
	
	# Wait for ASR result
	name = pa + args["@index"].value + ".xml"
	time.sleep(0.25)
	while not os.path.exists(name+"_done"):
		time.sleep(0.05)
	if os.path.exists(name):
		tree = ET.parse(name)
		root = tree.getroot()
		work(root, result)
				
print json.dumps(result)

