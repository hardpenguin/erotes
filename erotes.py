#!/usr/bin/python2.7

import os
import sys

import erotes_start_project
import erotes_run_project
import erotes_export_project
import erotes_utils

ErotesDir=os.path.dirname(os.path.abspath(sys.argv[0])) # where does the script reside
CurrentDir=os.getcwd() # where is the script executed

ErotesConfig=erotes_utils.config.ConfigFile(ErotesDir+"/config.json").Read() # read the config

Arguments=erotes_utils.arguments.Arguments(sys.argv) # read arguments

for HelpLine in erotes_utils.helplines.HelpLines: # create help
    Arguments.AddArgument(HelpLine[0],HelpLine[1],HelpLine[2])

if len(Arguments.Args)<2:
    Arguments.DisplayHelp()
    sys.exit()

Mode=Arguments.ChooseFirstArgument() # decide what we're doing

if (Mode==Arguments.SupportedArgs[0]["short"]) or \
   (Mode==Arguments.SupportedArgs[0]["long"]): # start
    erotes_start_project.CreateWorkplace(ErotesDir+"/templates/"+ErotesConfig["template"], \
                                            ErotesConfig["template"], \
                                            ErotesConfig, \
                                            CurrentDir)
    erotes_start_project.DownloadAndUnpackLove(ErotesConfig,CurrentDir)

elif (Mode==Arguments.SupportedArgs[1]["short"]) or \
     (Mode==Arguments.SupportedArgs[1]["long"]): # run
    erotes_run_project.RunWorkplace(CurrentDir)

elif (Mode==Arguments.SupportedArgs[2]["short"]) or \
     (Mode==Arguments.SupportedArgs[2]["long"]): # export
    erotes_export_project.ExportProject(ErotesConfig["platforms"],CurrentDir)

else: # help
    Arguments.DisplayHelp()