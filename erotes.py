#!/usr/bin/python2.7

import os
import sys

import erotes_start_project
import erotes_run_project
import erotes_export_project
import erotes_utils

ErotesDir=os.path.dirname(os.path.abspath(sys.argv[0]))
CurrentDir=os.getcwd()

ErotesConfig=erotes_utils.config.ConfigFile(ErotesDir+"/config.json").Read()

erotes_start_project.CreateWorkplace(ErotesDir+"/templates/"+ErotesConfig["template"], \
                                            ErotesConfig["template"], \
                                            ErotesConfig, \
                                            CurrentDir)
erotes_start_project.DownloadAndUnpackLove(ErotesConfig,CurrentDir)

erotes_run_project.RunWorkplace(CurrentDir)

erotes_export_project.ExportProject(ErotesConfig["platforms"],CurrentDir)