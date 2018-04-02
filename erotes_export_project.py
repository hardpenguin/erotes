#!/usr/bin/python2.7

import os
import libarchive
import distutils.file_util
import shutil

import erotes_utils

def ExportLove(WorkDir,ProjectName):
    os.chdir(WorkDir+"/workplace")
    List=os.listdir('.')
    ExportPath=erotes_utils.directory_utils \
                           .Folder(WorkDir+"/export") \
                           .Create()

    print "Creating .love file..."
    LoveFile=erotes_utils.archive \
                         .ArchiveFile(ExportPath+"/"+ProjectName+".love") \
                         .PackageFiles(List) # create .love file

    return(LoveFile)

def ExportPlatform(WorkDir,ProjectName,Platform):
    ExportPath=WorkDir+"/export/"
    LovePath=WorkDir+"/love/"+Platform+"/"
    LoveFiles=os.listdir(LovePath)
    if "linux" in Platform:
        LoveBinary="love"
    elif "windows" in Platform:
        LoveBinary="love.exe"
    LoveBinaryPath=ExportPath+LoveBinary
    if "linux" in Platform:
        GameBinary=ProjectName
    elif "windows" in Platform:
        GameBinary=ProjectName+".exe"
    GameBinaryPath=ExportPath+GameBinary
    LoveFile=ExportPath+ProjectName+".love"

    print "Creating "+Platform+" export..."
    for Each in LoveFiles:
        CurrentFile=LovePath+Each
        if os.path.islink(CurrentFile):
            erotes_utils.symlink_utils \
                        .Symlink(ExportPath+"/"+Each) \
                        .Create(CurrentFile)
        else:
            distutils.file_util \
                     .copy_file(LovePath+Each,ExportPath)

    erotes_utils.concatenation \
                .Object(GameBinaryPath) \
                .Concatenate(LoveBinaryPath, \
                  LoveFile)

    if "linux" in Platform:
        os.chmod(GameBinaryPath, 0775)

    ToPackage=list(LoveFiles)
    ToPackage.append(GameBinary)
    ToRemove=list(ToPackage)
    ToPackage.remove(LoveBinary)
    PackagePath=ExportPath+"/"+ProjectName+"-"+Platform+".zip"

    os.chdir(ExportPath)
    ExportPackage=erotes_utils.archive \
                              .ArchiveFile(PackagePath) \
                              .PackageFiles(ToPackage)

    for Each in ToRemove:
        os.remove(ExportPath+Each)    

def ExportProject(Platforms,WorkDir):
    print "Starting exports..."
    ProjectName="game"
    ExportLove(WorkDir,ProjectName)

    if "linux64" in Platforms:
        ExportPlatform(WorkDir,ProjectName,"linux64")
    if "windows32" in Platforms:
        ExportPlatform(WorkDir,ProjectName,"windows32")

    print "Done."