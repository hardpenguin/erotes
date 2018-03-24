#!/usr/bin/python2.7

# standard library
import os
import sys

# project modules
import start_project
import run_project
import export_project
import config

ErotesDir=os.path.dirname(os.path.abspath(sys.argv[0]))
CurrentDir=os.getcwd()

ErotesConfig=config.ConfigFile(ErotesDir+"/config.json").Read()

start_project.CreateWorkplace(ErotesDir+"/templates/"+ErotesConfig["template"], \
                                            ErotesConfig["template"], \
                                            ErotesConfig, \
                                            CurrentDir)
start_project.DownloadAndUnpackLove(ErotesConfig,CurrentDir)
