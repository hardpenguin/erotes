#!/usr/bin/python2.7

# standard library
import os
import sys

# project modules
import start_project
import run_project
import export_project
import config

ScriptDir=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(ScriptDir)

ErotesConfig=config.ConfigFile(ScriptDir+"/config.json").Read()

start_project.CreateWorkplace(ScriptDir+"/templates/"+ErotesConfig["template"], \
                                            ErotesConfig["template"], \
                                            ErotesConfig, \
                                            ScriptDir)
start_project.DownloadAndUnpackLove(ErotesConfig,ScriptDir)
