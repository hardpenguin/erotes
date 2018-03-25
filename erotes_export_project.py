#!/usr/bin/python2.7

import os
import libarchive

import erotes_utils

# just a stub
def ExportProject(WorkDir):

    os.chdir(WorkDir+"/workplace")
    List=os.listdir('.')

    erotes_utils.created_folder.CreatedFolder(WorkDir+"/downloads/"+Platform).Create()
    
    # move below to a new class
    with libarchive.file_writer(ExportPath+'/game.love', 'zip') as archive:
      for Every in (List):
        archive.add_files(Every)