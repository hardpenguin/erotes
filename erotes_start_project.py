#!/usr/bin/python2.7

import os
import distutils.dir_util
import distutils.file_util

import erotes_utils

def CreateWorkplace(TemplateSource,WorkDir):
    TemplateName=TemplateSource.split("/")[-1]
    WorkplacePath=WorkDir+"/workplace"

    print "Creating workplace from \""+TemplateName+"\" template..."
    distutils.dir_util \
             .copy_tree(TemplateSource,WorkplacePath)

    print "Done."


def DownloadLove(Link,Platform,PlatformPath):
    DownloadedPackage=erotes_utils.download_utils \
                                  .Downloadable(Link["link"])
    DownloadDestination=PlatformPath+"/"+DownloadedPackage.Name

    print "Downloading "+DownloadedPackage.Name+"..."
    DownloadedPackage.Download(DownloadDestination)

    return(DownloadedPackage.Name) 

def UnpackLove(PackageName,Platform,PlatformPath):
    PackageBasename=PackageName.replace(".deb","").replace(".zip","")
    TargetPath=erotes_utils.directory_utils \
                           .Folder(PlatformPath+"/"+PackageBasename) \
                           .Create()
    os.chdir(TargetPath)

    print "Unpacking "+PackageName+"..."
    erotes_utils.archive \
                .ArchiveFile(PlatformPath+"/"+PackageName) \
                .Unpack()

    if "linux" in Platform:
        erotes_utils.archive \
                    .ArchiveFile(TargetPath+"/data.tar.xz") \
                    .Unpack()

def CopyRuntime(Platform,PlatformPath):
    for Root, Dirs, Files in os.walk(PlatformPath):
        for File in Files:
            if "linux" in Platform:
                if ("/usr/bin" in Root) or ("/usr/lib" in Root):
                    distutils.file_util \
                             .copy_file(Root+"/"+File,PlatformPath)
            elif "windows" in Platform:
                if ("love.exe" in Files):
                    distutils.file_util \
                             .copy_file(Root+"/"+File,PlatformPath)
                

def StartProject(ErotesConfig,WorkDir):
    Template=ErotesConfig["template"]
    TemplatePath=WorkDir+"/templates/"+Template
    CreateWorkplace(TemplatePath,WorkDir)

    for Platform in ErotesConfig["platforms"]:
        DownloadsPlatformPath=erotes_utils.directory_utils \
                                          .Folder(WorkDir+"/downloads/"+Platform) \
                                          .Create()
        LovePlatformPath=erotes_utils.directory_utils \
                                     .Folder(WorkDir+"/love/"+Platform) \
                                     .Create()
        for Link in ErotesConfig["links"]:
            os.chdir(WorkDir)
            if Link["platform"]==Platform:
                FileDownloaded=DownloadLove(Link,Platform,DownloadsPlatformPath)
                UnpackLove(FileDownloaded,Platform,DownloadsPlatformPath)
                CopyRuntime(Platform,LovePlatformPath)

    print "Done."