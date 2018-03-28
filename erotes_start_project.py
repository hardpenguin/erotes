#!/usr/bin/python2.7

import os
import distutils.dir_util
import distutils.file_util

import erotes_utils

def CreateWorkplace(TemplateSource,TemplateName,WorkDir):

    print "Creating workplace from \""+TemplateName+"\" template..."
    distutils.dir_util.copy_tree(TemplateSource,WorkDir+"/workplace")
    print "Done."


def DownloadAndUnpackLove(ErotesConfig,WorkDir):

    for Platform in ErotesConfig["platforms"]:
        PlatformPath=erotes_utils.created_folder.CreatedFolder(WorkDir+"/downloads/"+Platform).Create()
        erotes_utils.created_folder.CreatedFolder(WorkDir+"/love/"+Platform).Create()
        for Link in ErotesConfig["links"]:
            os.chdir(WorkDir)
            if Link["platform"]==Platform:

                DownloadedPackage=erotes_utils.downloaded_file.DownloadedFile(Link["link"])          
                print "Downloading "+DownloadedPackage.Name+"..."
                DownloadedPackage.Download(PlatformPath+"/"+DownloadedPackage.Name)

                DownloadedPackageContentsPathName=DownloadedPackage.Name.replace(".deb","").replace(".zip","")
                DownloadedPackageContentsPath=erotes_utils.created_folder \
                                    .CreatedFolder(WorkDir+"/downloads/"+Platform+"/"+DownloadedPackageContentsPathName) \
                                    .Create()
                os.chdir(DownloadedPackageContentsPath)
                print "Unpacking "+DownloadedPackage.Name+"..."
                
                erotes_utils.archive.Archive(PlatformPath+"/"+DownloadedPackage.Name).Unpack()

                if "linux" in Link["platform"]:
                    erotes_utils.archive.Archive(DownloadedPackageContentsPath+"/data.tar.xz").Unpack()

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
