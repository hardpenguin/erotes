#!/usr/bin/python2.7

import sys
import os

import urllib
import json

import libarchive

ScriptDir=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(ScriptDir)

class DownloadedFile(object): # file to be downloaded from a specified URL
    
    def __init__(self,Link):
        self.Link=Link
        self.Name=self.Link.split("downloads/")[1] # determine the target name for urlretrieve

    def Download(self,Destination): # downloads the file from object defined URL to specified path
        self.Destination=Destination
        urllib.urlretrieve(self.Link,self.Destination)
        # I gave up on handling download errors as bitbucket willingly serves a HTML file for wrong links

class CreatedFolder(object): # folder to be created, needs name

    def __init__(self,Path):
        self.Path=Path

    def Create(self): # creates folder with a object defined name in a specified path
        if not os.path.exists(self.Path):
            os.makedirs(self.Path)
        return(self.Path)

class ConfigFile(object): # config file to be loaded and read

    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Read(self):
        with open(self.FilePath, 'r') as File:
            return(json.load(File))

class UnpackedArchive(object): # archive to be unpacked
    
    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Unpack(self):
        libarchive.extract_file(self.FilePath)

ErotesConfig=ConfigFile(ScriptDir+"/defaults/config.json").Read()

for Platform in ErotesConfig["platforms"]:
    PlatformPath=CreatedFolder(ScriptDir+"/love/"+Platform).Create()
    for Link in ErotesConfig["links"]:
        os.chdir(ScriptDir)
        if Link["platform"]==Platform:

            Archive=DownloadedFile(Link["link"])          
            print "Downloading "+Archive.Name+"..."
            Archive.Download(PlatformPath+"/"+Archive.Name)

            ArchiveContentsPathName=Archive.Name.replace(".deb","").replace(".zip","")
            ArchiveContentsPath=CreatedFolder(ScriptDir+"/love/"+Platform+"/"+ArchiveContentsPathName).Create()
            os.chdir(ArchiveContentsPath)
            print "Unpacking "+Archive.Name+"..."
            UnpackedArchive(PlatformPath+"/"+Archive.Name).Unpack()

print "Done."