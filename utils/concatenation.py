import os

class Object(object): # archive to be unpacked
    
    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Concatenate(self,Input1,Input2):
        with open(self.FilePath, "wb") as OutFile:
            for Part in [Input1,Input2]:
                with open(Part, "rb") as InFile:
                    OutFile.write(InFile.read())
                InFile.close()
        OutFile.close()
