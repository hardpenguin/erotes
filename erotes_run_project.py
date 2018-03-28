#!/usr/bin/python2.7

import os

def RunWorkplace(WorkDir):
    RuntimeSubpath="/love/linux64/"
    RuntimeBinary="love"

    LdLibraryPath="LD_LIBRARY_PATH=\"${LD_LIBRARY_PATH}:"+WorkDir+RuntimeSubpath+"\""
    Executable="\""+WorkDir+RuntimeSubpath+RuntimeBinary+"\""
    Argument="\""+WorkDir+"/workplace\""
    RunCommand=LdLibraryPath+" "+Executable+" "+Argument

    print "Running project..."
    os.system(RunCommand)
    print "Done."