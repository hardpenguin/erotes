import json

class ConfigFile(object): # config file to be loaded and read

    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Read(self):
        with open(self.FilePath, 'r') as File:
            return(json.load(File))