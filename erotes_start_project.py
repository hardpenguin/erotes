#!/usr/bin/python2.7

import os
import distutils.dir_util
import distutils.file_util

import erotes_utils

def CreateWorkplace(TemplateSource,WorkDir):
    TemplateName=TemplateSource.split("/")[-1]
    print "Creating workplace from \""+TemplateName+"\" template..."
    distutils.dir_util.copy_tree(TemplateSource,WorkDir+"/workplace")
    print "Done."


def DownloadAndUnpackLove(ErotesConfig,WorkDir):
    for Platform in ErotesConfig["platforms"]:
        PlatformPath=erotes_utils.directory_utils.Folder(WorkDir+"/downloads/"+Platform).Create()
        erotes_utils.directory_utils.Folder(WorkDir+"/love/"+Platform).Create()
        for Link in ErotesConfig["links"]:
            os.chdir(WorkDir)
            if Link["platform"]==Platform:
                DownloadedPackage=erotes_utils.download_utils.Downloadable(Link["link"])          
                print "Downloading "+DownloadedPackage.Name+"..."
                DownloadedPackage.Download(PlatformPath+"/"+DownloadedPackage.Name)

                DownloadedPackageContentsPathName=DownloadedPackage.Name.replace(".deb","").replace(".zip","")
                DownloadedPackageContentsPath=erotes_utils.directory_utils \
                                    .Folder(WorkDir+"/downloads/"+Platform+"/"+DownloadedPackageContentsPathName) \
                                    .Create()
                os.chdir(DownloadedPackageContentsPath)
                print "Unpacking "+DownloadedPackage.Name+"..."
                
                erotes_utils.archive.ArchiveFile(PlatformPath+"/"+DownloadedPackage.Name).Unpack()

                if "linux" in Link["platform"]:
                    erotes_utils.archive.ArchiveFile(DownloadedPackageContentsPath+"/data.tar.xz").Unpack()

                    for Root, Dirs, Files in os.walk(DownloadedPackageContentsPath):
                        for File in Files:
                            if ("/usr/bin" in Root) or ("/usr/lib" in Root):
                                distutils.file_util.copy_file(Root+"/"+File,WorkDir+"/love/"+Platform)

                elif "windows" in Link["platform"]:
                    
                    for Root, Dirs, Files in os.walk(DownloadedPackageContentsPath):
                        for File in Files:
                            if ("love.exe" in Files):
                                distutils.file_util.copy_file(Root+"/"+File,WorkDir+"/love/"+Platform)

    print "Done."
