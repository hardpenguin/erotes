#!/usr/bin/python2.7

# standard library
import os

# project modules
import config
import created_folder
import downloaded_file
import unpacked_archive

def StartProject(ConfigPath,WorkDir):

    ErotesConfig=config.ConfigFile(ConfigPath).Read()

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