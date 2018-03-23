#!/usr/bin/python2.7

# standard library
import os
import distutils.dir_util

# project modules
import created_folder
import downloaded_file
import unpacked_archive

def CreateWorkplace(TemplateSource,TemplateName,ErotesConfig,WorkDir):

    print "Creating workplace from \""+TemplateName+"\" template..."
    distutils.dir_util.copy_tree(TemplateSource,WorkDir+"/workplace")
    print "Done."


def DownloadLove(ErotesConfig,WorkDir):

    for Platform in ErotesConfig["platforms"]:
        PlatformPath=created_folder.CreatedFolder(WorkDir+"/love/"+Platform).Create()
        for Link in ErotesConfig["links"]:
            os.chdir(WorkDir)
            if Link["platform"]==Platform:

                Archive=downloaded_file.DownloadedFile(Link["link"])          
                print "Downloading "+Archive.Name+"..."
                Archive.Download(PlatformPath+"/"+Archive.Name)

                ArchiveContentsPathName=Archive.Name.replace(".deb","").replace(".zip","")
                ArchiveContentsPath=created_folder.CreatedFolder(WorkDir+"/love/"+Platform+"/"+ArchiveContentsPathName).Create()
                os.chdir(ArchiveContentsPath)
                print "Unpacking "+Archive.Name+"..."
                unpacked_archive.UnpackedArchive(PlatformPath+"/"+Archive.Name).Unpack()

    print "Done."
