#!/usr/bin/python2.7

import sys
import os

import urllib
            
ScriptDir=os.path.dirname(os.path.abspath(sys.argv[0]))

print "Downloading love..."
LoveFolder="love"
if not os.path.exists(ScriptDir+"/"+LoveFolder):
    os.makedirs(ScriptDir+"/"+LoveFolder)
Link="https://bitbucket.org/rude/love/downloads/love_0.10.2ppa1_amd64.deb"
FileName=Link.split("downloads/")[1]
urllib.urlretrieve(Link,ScriptDir+"/"+LoveFolder+"/"+FileName)