import libarchive

class UnpackedArchive(object): # archive to be unpacked
    
    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Unpack(self):
        libarchive.extract_file(self.FilePath)