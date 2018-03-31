#!/usr/bin/python2.7

import os
import sys
import distutils.dir_util
import distutils.file_util

import erotes_utils

ErotesDir=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(ErotesDir)

Options=sys.argv[1:]
if len(Options)<1:
    print "Building in regular mode..."
    Mode="regular"
elif "--release" in Options:
    print "Building in release mode..."
    Mode="release"
else:
    print "Unknown option!"
    sys.exit()

ReleaseVersion="1.0"
BuildVersion=erotes_utils.versioning \
                         .Version("version") \
                         .GenerateVersion(ReleaseVersion)

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
             .copy_tree(Each,DistributablePath+"/"+Each)

if Mode=="release":
    print "Packaging distributable..."
    os.chdir(DistributablePath)
    List=os.listdir(".")
    LinuxDistPackageName=ErotesDir+"/erotes-linux-"+BuildVersion+".tar.gz"
    LinuxDistPackage=erotes_utils.archive \
                                 .ArchiveFile(LinuxDistPackageName) \
                                 .PackageFiles(List,"ustar","gzip")



print "Done."