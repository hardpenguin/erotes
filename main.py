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

ErotesConfig=config.config.ConfigFile(ScriptDir+"/config.json").Read()

start_project.start_project.StartProject(ErotesConfig,ScriptDir)
