import time

class Version(object):
    
    def __init__(self,VersionFilePath):
        self.VersionFilePath=VersionFilePath

    def GetVersion(self):
        VersionFile=open(self.VersionFilePath,"r")
        VersionNumber=VersionFile.read()
        VersionFile.close()
        return(VersionNumber)

    def GenerateVersion(self,VersionNumber):
        EpochDays=str(time.time()/60/60/24).split(".")[0]
        VersionFile=open(self.VersionFilePath,"w")
        VersionFile.write(str(VersionNumber) \
                          +"." \
                          +EpochDays)
        VersionFile.close()
        return(self.GetVersion())