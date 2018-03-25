#!/usr/bin/python2.7

import os
import libarchive

import erotes_utils

def ExportProject(Platforms,WorkDir):

    os.chdir(WorkDir+"/workplace")
    List=os.listdir('.')

    ExportPath=erotes_utils.created_folder.CreatedFolder(WorkDir+"/export").Create()
    print "Creating .love file..."
    LoveFile=erotes_utils.created_zip.CreatedZip(List,ExportPath).PackageContents() # create .love file

    """if "linux64" in Platforms: # create Linux build
                    with open("binary_file_1", "ab") as myfile, open("binary_file_2", "rb") as file2:
                        myfile.write(file2.read())
            
                elif "windows32" in Platforms: # create Windows build
                    """


    print "Done."