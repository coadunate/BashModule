#!/usr/bin/python 

import json 
import sys
import yaml 

input = json.load(sys.stdin)
print input
print "" 
print "" 

yamput = yaml.load(json.dumps(input))
print yaml.dump(yamput, default_flow_style=False, default_style='')

outputString = ""
for key in input:
  print input[key] 
  outputString += key + " "
  for tag in input[key]: 
    if len(tag) > 1: 
      outputString += "--" + tag + " " +  input[key][tag] + " "
      print outputString
    else: 
      outputString += "-" + tag + " " + input[key][tag] + " "
      print outputString



#print tag + " : " + input[key][tag]  
