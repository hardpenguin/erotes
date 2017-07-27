#!/usr/bin/python2.7

import sys
import os

import urllib

ScriptDir=os.path.dirname(os.path.abspath(sys.argv[0]))

class DownloadedFile(object): # downloads the file from a chosen URL and checks its name
    
    def __init__(self,Link):
        self.Link=Link
        self.Name=self.Link.split("downloads/")[1]

    def Download(self,Destination):
        self.Destination=Destination
        urllib.urlretrieve(self.Link,self.Destination)
        # I gave up on handling download errors as bitbucket willingly serves a HTML file for wrong links

class CreatedFolder(object): # creates folder and returns its absolute path

    def __init__(self,Name):
        self.Name=Name

    def Create(self,Path):
        self.Path=Path
        if not os.path.exists(self.Path+"/"+self.Name):
            os.makedirs(self.Path+"/"+self.Name)
        return(self.Path+"/"+self.Name)

LovePath=CreatedFolder("love").Create(ScriptDir)

LinksForDownload=[
                    "https://bitbucket.org/rude/love/downloads/love_0.10.2ppa1_amd64.deb",
                    "https://bitbucket.org/rude/love/downloads/liblove0_0.10.2ppa1_amd64.deb"
                 ]

for Link in LinksForDownload:
    D=DownloadedFile(Link)
    D.Download(LovePath+"/"+D.Name)
    print "Downloading "+D.Name+"..."