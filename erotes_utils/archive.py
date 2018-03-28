import libarchive

class Archive(object): # archive to be unpacked
    
    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Unpack(self):
        libarchive.extract_file(self.FilePath)

    def PackageFiles(self,FilesList,Format="zip"):
        if Format=="zip":
            with libarchive.file_writer(self.FilePath,"zip") as Package:
              for Every in (FilesList):
                Package.add_files(Every)