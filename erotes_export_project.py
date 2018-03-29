#!/usr/bin/python2.7

import os
import libarchive

import erotes_utils

def ExportLove(WorkDir):
    os.chdir(WorkDir+"/workplace")
    List=os.listdir('.')
    ExportPath=erotes_utils.directory_utils \
                           .Folder(WorkDir+"/export") \
                           .Create()

    print "Creating .love file..."
    LoveFile=erotes_utils.archive \
                         .ArchiveFile(ExportPath+"/game.love") \
                         .PackageFiles(List) # create .love file

    print "Done."

def ExportProject(Platforms,WorkDir):
    ExportLove(WorkDir)


# def ExportLinux():
# def ExportWindows():

    """if "linux64" in Platforms: # create Linux build
                    with open("binary_file_1", "ab") as myfile, open("binary_file_2", "rb") as file2:
                        myfile.write(file2.read())
            
                elif "windows32" in Platforms: # create Windows build
                    """