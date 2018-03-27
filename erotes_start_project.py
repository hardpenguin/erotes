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
        PlatformPath = erotes_utils.created_folder.CreatedFolder(WorkDir+"/downloads/"+Platform).Create()
        erotes_utils.created_folder.CreatedFolder(WorkDir+"/love/"+Platform).Create()
        for Link in ErotesConfig["links"]:
            os.chdir(WorkDir)
            if Link["platform"] == Platform:

                Archive = erotes_utils.downloaded_file.DownloadedFile(Link["link"])          
                ArchivePath = PlatformPath + "/" + Archive.Name
                DownloadDestination = WorkDir + "/downloads/" + Platform + "/" + ArchiveContentsPathName

                print "Downloading " + Archive.Name + "..."

                Archive.Download(ArchivePath)
                ArchiveContentsPathName = Archive.Name.replace(".deb", "").replace(".zip", "")
                ArchiveContentsPath = erotes_utils.created_folder.CreatedFolder(DownloadDestination).Create()
                os.chdir(ArchiveContentsPath)

                print "Unpacking " + Archive.Name + "..."

                erotes_utils.unpacked_archive.UnpackedArchive(ArchivePath).Unpack()
                if IsLinux(Link):
                    erotes_utils.unpacked_archive.UnpackedArchive(ArchiveContentsPath + "/data.tar.xz").Unpack()

                DestinationFolder = WorkDir + "/love/" + Platform

                CopyArchive(ArchiveContentsPath, DestinationFolder)
                    
    def CopyArchive(Path, DestinationFolder):
        for Root, Dirs, Files in os.walk(Path):
            if HaveExecutable(Files, Root):
                FilePath = Root + "/"
                
                CopyFiles(Files, DestinationFolder, FilePath)
    
    def HaveExecutable(Files, Root):
        return (("love.exe" in Files) or ("/usr/bin" in Root) or ("/usr/lib" in Root))
    
    def CopyFiles(Files, DestinationFolder, FilePath):
        for FileName in Files:
            distutils.file_util.copy_file(FilePath + FileName, DestinationFolder)
            
    def IsLinux(Link):
        return "linux" in Link["platform"]
    
    print "Done."
