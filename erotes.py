#!/usr/bin/python2.7

import os
import sys

import start
import run
import export
import utils

ErotesDir=os.path.dirname(os.path.abspath(sys.argv[0])) # where does the script reside
CurrentDir=os.getcwd() # where is the script executed

ErotesConfig=utils.config \
                         .ConfigFile(ErotesDir+"/config.json") \
                         .Read() # read the config
Platforms=ErotesConfig["platforms"]

Arguments=utils.arguments.Arguments(sys.argv) # read arguments

for Option in utils.options.Options: # create options
    Arguments.AddArgument(Option[0], \
                          Option[1], \
                          Option[2])

Mode=utils.modes \
                 .SelectMode(Arguments) # decide what we're doing

if (Mode=="start"): # start
    start.StartProject(ErotesConfig,CurrentDir)

elif (Mode=="run"): # run
    run.RunWorkplace(CurrentDir)

elif (Mode=="export"): # export
    export.ExportProject(ErotesConfig,CurrentDir)

else: # help
    Arguments.DisplayHelp()