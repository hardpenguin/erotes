#!/usr/bin/python2.7

import os
import libarchive
import distutils.file_util
import re

import utils

def ExportLove(WorkDir,NameString,VersionString):
    Blacklisted=[".git",".gitignore"]
    os.chdir(WorkDir+"/workplace")
    List=os.listdir('.')
    for Each in Blacklisted:
        if Each in List:
            List.remove(Each)
    ExportPath=utils.directory_utils \
                           .Folder(WorkDir+"/export") \
                           .Create()

    LoveFilePath=ExportPath+"/"+NameString+"_"+VersionString+".love"

    print "Creating .love file..."
    LoveFile=utils.archive \
                         .ArchiveFile(LoveFilePath) \
                         .PackageFiles(List) # create .love file

    return(LoveFile)

def ExportPlatform(WorkDir,NameString,VersionString,Platform):
    ExportPath=WorkDir+"/export/"
    LovePath=WorkDir+"/love/"+Platform+"/"
    LoveFiles=os.listdir(LovePath)
    if "linux" in Platform:
        LoveBinary="love"
    elif "windows" in Platform:
        LoveBinary="love.exe"
    LoveBinaryPath=ExportPath+LoveBinary
    if "linux" in Platform:
        GameBinary=NameString
    elif "windows" in Platform:
        GameBinary=NameString+".exe"
    GameBinaryPath=ExportPath+GameBinary
    LoveFile=ExportPath+NameString+"_"+VersionString+".love"

    print "Creating "+Platform+" export..."
    for Each in LoveFiles:
        CurrentFile=LovePath+Each
        if os.path.islink(CurrentFile):
            utils.symlink_utils \
                        .Symlink(ExportPath+"/"+Each) \
                        .Create(CurrentFile)
        else:
            distutils.file_util \
                     .copy_file(LovePath+Each,ExportPath)

    utils.concatenation \
                .Object(GameBinaryPath) \
                .Concatenate(LoveBinaryPath, \
                  LoveFile)

    if "linux" in Platform:
        os.chmod(GameBinaryPath, 0775)

    ToPackage=list(LoveFiles)
    ToPackage.append(GameBinary)
    ToRemove=list(ToPackage)
    ToPackage.remove(LoveBinary)
    PackagePath=ExportPath+"/"+NameString+"_"+VersionString+"_"+Platform+".zip"

    os.chdir(ExportPath)
    ExportPackage=utils.archive \
                              .ArchiveFile(PackagePath) \
                              .PackageFiles(ToPackage)

    for Each in ToRemove:
        os.remove(ExportPath+Each)    

def ExportProject(ErotesConfig,WorkDir):
    print "Starting exports..."
    ProjectName=ErotesConfig["name"]
    ProjectVersion=ErotesConfig["version"]
    NameString=re.sub("[^0-9a-zA-Z]+","_",ProjectName).lower()
    VersionString=re.sub("[^0-9a-zA-Z]+","_",ProjectVersion)
    Platforms=ErotesConfig["platforms"]
    ExportLove(WorkDir,NameString,VersionString)

    if "linux64" in Platforms:
        ExportPlatform(WorkDir,NameString,VersionString,"linux64")
    if "windows32" in Platforms:
        ExportPlatform(WorkDir,NameString,VersionString,"windows32")

    print "Done."