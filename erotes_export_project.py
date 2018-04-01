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

    print "Done."

    return(LoveFile)

def ExportLinux(WorkDir,ProjectName):
    ExportPath=WorkDir+"/export/"
    LinuxLovePath=WorkDir+"/love/linux64/"
    LinuxLoveFiles=os.listdir(LinuxLovePath)
    LinuxLoveBinary=ExportPath+"love"
    LinuxGameBinary=ExportPath+ProjectName
    LoveFile=ExportPath+ProjectName+".love"

    print "Creating Linux export..."
    for Each in LinuxLoveFiles:
        CurrentFile=LinuxLovePath+Each
        if os.path.islink(CurrentFile):
            erotes_utils.symlink_utils \
                        .Symlink(ExportPath+"/"+Each) \
                        .Create(CurrentFile)
        else:
            distutils.file_util \
                     .copy_file(LinuxLovePath+Each,ExportPath)

    erotes_utils.concatenation \
                .Object(LinuxGameBinary) \
                .Concatenate(LinuxLoveBinary, \
                  LoveFile)

    os.chmod(LinuxGameBinary, 0775)

    # ToPackage=LinuxLoveFiles
    # ToPackage.append(LinuxGameBinary)

    # LinuxPackage=erotes_utils.archive \
    #                          .ArchiveFile(ExportPath+"/"+ProjectName+"-linux64.zip") \
    #                          .PackageFiles(ToPackage)

    # for Each in ToPackage:
    #     os.remove(ExportPath+Each)

    print "Done."    

def ExportWindows(WorkDir,ProjectName):
    pass

def ExportProject(Platforms,WorkDir):
    ProjectName="game"
    ExportLove(WorkDir,ProjectName)

    if "linux64" in Platforms:
        ExportLinux(WorkDir,ProjectName)
    elif "windows32" in Platforms:
        ExportWindows(WorkDir,ProjectName)
