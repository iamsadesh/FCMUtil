# -*- coding: utf-8 -*-

from urllib2 import *
import urllib
import json
import sys

MY_API_KEY="{Your API Key}"

messageTitle = sys.argv[1]
messageBody = sys.argv[2]

fname = sys.argv[3]

with open(fname) as file:
    content = [x.strip('\n') for x in file.readlines()]
	
file.close()

for line in content:
	print line

for token in content:
    data = {"to" : token,"priority" : "high","data" : {"body" : messageBody,"title" : messageTitle,"icon" : "ic_launcher","type":"new_message"}}
    dataAsJSON = json.dumps(data)
    request = Request("https://fcm.googleapis.com/fcm/send",dataAsJSON,{ "Authorization" : "key="+MY_API_KEY,"Content-type" : "application/json"})
    print urlopen(request).read()
