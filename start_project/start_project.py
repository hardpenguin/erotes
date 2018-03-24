#!/usr/bin/python2.7

# standard library
import os
import distutils.dir_util
import distutils.file_util

# project modules
import created_folder
import downloaded_file
import unpacked_archive

def CreateWorkplace(TemplateSource,TemplateName,ErotesConfig,WorkDir):

    print "Creating workplace from \""+TemplateName+"\" template..."
    distutils.dir_util.copy_tree(TemplateSource,WorkDir+"/workplace")
    print "Done."


def DownloadAndUnpackLove(ErotesConfig,WorkDir):

    for Platform in ErotesConfig["platforms"]:
        PlatformPath=created_folder.CreatedFolder(WorkDir+"/downloads/"+Platform).Create()
        created_folder.CreatedFolder(WorkDir+"/love/"+Platform).Create()
        for Link in ErotesConfig["links"]:
            os.chdir(WorkDir)
            if Link["platform"]==Platform:

                Archive=downloaded_file.DownloadedFile(Link["link"])          
                print "Downloading "+Archive.Name+"..."
                Archive.Download(PlatformPath+"/"+Archive.Name)

                ArchiveContentsPathName=Archive.Name.replace(".deb","").replace(".zip","")
                ArchiveContentsPath=created_folder.CreatedFolder(WorkDir+"/downloads/"+Platform+"/"+ArchiveContentsPathName).Create()
                os.chdir(ArchiveContentsPath)
                print "Unpacking "+Archive.Name+"..."
                
                unpacked_archive.UnpackedArchive(PlatformPath+"/"+Archive.Name).Unpack()

                if "linux" in Link["platform"]:
                    unpacked_archive.UnpackedArchive(ArchiveContentsPath+"/data.tar.xz").Unpack()

                    for Root, Dirs, Files in os.walk(ArchiveContentsPath):
                        for File in Files:
                            if ("/usr/bin" in Root) or ("/usr/lib" in Root):
                                distutils.file_util.copy_file(Root+"/"+File,WorkDir+"/love/"+Platform)

                elif "windows" in Link["platform"]:
                    
                    for Root, Dirs, Files in os.walk(ArchiveContentsPath):
                        for File in Files:
                            if ("love.exe" in Files):
                                distutils.file_util.copy_file(Root+"/"+File,WorkDir+"/love/"+Platform)



    print "Done."
