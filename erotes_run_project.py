#!/usr/bin/python2.7

import os

def RunWorkplace(WorkDir):

    RuntimeSubpath="/love/linux64/"
    RuntimeBinary="love"

    print "Running project..."
    os.system("LD_LIBRARY_PATH=\"$LD_LIBRARY_PATH:"+WorkDir+RuntimeSubpath+"\" "+WorkDir+RuntimeSubpath+RuntimeBinary+" "+WorkDir+"/workplace")
    print "Done."