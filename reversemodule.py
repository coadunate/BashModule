#!/usr/bin/python 
import sys 
import shlex 
import json
#import ruamel.yaml
import pyaml
import itertools
import collections
import yaml

#open file for reading or read from standard in 
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin    
for line in f:
  #tokenize input 
  myline = line.rstrip('\n')
  moreline1 = shlex.split(myline)
  if len(moreline1) == 0: 
    break
  moreline = [i.decode('UTF-8') for i in moreline1]
  #print moreline
  #convert strings to unicode 
  #begin creating json 
  #myCommand = {u"commandline": {"name": moreline[0]}}
  myCommand = {u"commandline": collections.OrderedDict()}
  myCommand[u"commandline"]["name"] = moreline[0]
  moreline.pop(0)
 # make iterator 
  while(len(moreline) > 0):
    #try block to deal with single last input
    try: 
      secondTerm = moreline[1]
    except:
      if moreline[0].startswith("-"):
        myCommand[u"commandline"][moreline[0][1:]] = ""
        moreline.pop(0)
        break
      elif moreline[0].startswith("--"):
        myCommand[u"commandline"][moreline[0][2:]] = ""
        moreline.pop(0)
        break
      else: 
        myCommand[u"commandline"][moreline[0]] = ""  
        moreline.pop(0)
        break
    if moreline[0].startswith("-") and not moreline[0].startswith("--"):
      if secondTerm.startswith("-") or secondTerm.startswith("--"): 
        #string slicing to remove "-" from string 
        commandInput = moreline[0][1:]
        myCommand[u"commandline"][commandInput] = ""
        moreline.pop(0)
      else: 
        myCommand[u"commandline"][moreline[0][1:]] = moreline[1]
        moreline.pop(0)
        moreline.pop(0)
    elif moreline[0].startswith("--"):
      if secondTerm.startswith("-") or secondTerm.startswith("--"): 
        #string slicing to remove "-" from string 
        commandInput = moreline[0][2:]
        myCommand[u"commandline"][commandInput] = ""
        moreline.pop(0)
      else:
        commandInput = moreline[0][2:]
        myCommand[u"commandline"][commandInput] = moreline[1]
        moreline.pop(0)
        moreline.pop(0)
    else: 
      myCommand[u"commandline"][moreline[0]] = ""
      moreline.pop(0)
  #print yaml.dump(myCommand, explicit_start=True)
  #ruamel.yaml.dump(myCommand, sys.stdout)
 # myCommand[u"commandline"] = dict(myCommand[u"commandline"])
  #yaml = ruamel.yaml.YAML()
  #yaml.explicit_start = True
  yaml.dump(myCommand, sys.stdout)
  #json.dump(myCommand, sys.stdout)

