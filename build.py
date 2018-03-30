#!/usr/bin/python2.7

import os
import sys
import distutils.dir_util
import distutils.file_util

import erotes_utils

ErotesDir=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(ErotesDir)

PyInstallerExecutable="pyinstaller"
PyInstallerWorkPath="./pyinstaller/build"
PyInstallerDistPath="./pyinstaller/dist"
SpecFile="erotes.spec"
PyInstallerBuildCommand=PyInstallerExecutable \
                        + " --workpath=" \
                        + "\""+PyInstallerWorkPath+"\"" \
                        + " --distpath=" \
                        + "\""+PyInstallerDistPath+"\"" \
                        + " "+SpecFile

ExePath="pyinstaller/dist/erotes"
DistributablePath="dist"

SingleFiles=["config.json"]
Folders=["templates"]

print "Building executable with pyinstaller..."
print PyInstallerBuildCommand
os.system(PyInstallerBuildCommand)

print "Creating distributable folder..."
erotes_utils.directory_utils \
            .Folder(DistributablePath) \
            .Create()

print "Copying project executable..."
distutils.file_util \
         .copy_file(ExePath,DistributablePath)

print "Copying non-source files..."
for Each in SingleFiles:
    distutils.file_util \
         .copy_file(Each,DistributablePath)    

for Each in Folders:
    distutils.dir_util \
             .copy_tree(Each,DistributablePath)


print "Done."