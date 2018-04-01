import os

class Symlink(object): # archive to be unpacked
    
    def __init__(self,SymlinkPath):
        self.SymlinkPath=SymlinkPath

    def Create(self,SymlinkTo):
            LinkTo=os.readlink(SymlinkTo)
            if not os.path.exists(self.SymlinkPath):
                os.symlink(LinkTo,self.SymlinkPath)