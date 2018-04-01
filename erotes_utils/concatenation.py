import os

class Object(object): # archive to be unpacked
    
    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Concatenate(self,Input1,Input2):
        os.system("cat "+Input1+" "+Input2+" >"+self.FilePath)