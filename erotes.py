#!/usr/bin/python2.7

import os
import sys

import erotes_start_project
import erotes_run_project
import erotes_export_project
import erotes_utils

ErotesDir=os.path.dirname(os.path.abspath(sys.argv[0])) # where does the script reside
CurrentDir=os.getcwd() # where is the script executed

ErotesConfig=erotes_utils.config \
                         .ConfigFile(ErotesDir+"/config.json") \
                         .Read() # read the config
Platforms=ErotesConfig["platforms"]
Template=ErotesConfig["template"]
TemplatePath=ErotesDir+"/templates/"+Template

Arguments=erotes_utils.arguments.Arguments(sys.argv) # read arguments

for Option in erotes_utils.options.Options: # create options
    Arguments.AddArgument(Option[0], \
                          Option[1], \
                          Option[2])

Mode=erotes_utils.modes \
                 .SelectMode(Arguments) # decide what we're doing

if (Mode=="start"): # start
    erotes_start_project.CreateWorkplace(TemplatePath,CurrentDir)
    erotes_start_project.DownloadAndUnpackLove(ErotesConfig,CurrentDir)

elif (Mode=="run"): # run
    erotes_run_project.RunWorkplace(CurrentDir)

elif (Mode=="export"): # export
    erotes_export_project.ExportProject(Platforms,CurrentDir)

else: # help
    Arguments.DisplayHelp()