import libarchive

class ArchiveFile(object): # archive to be unpacked
    
    def __init__(self,FilePath):
        self.FilePath=FilePath

    def Unpack(self):
        libarchive.extract_file(self.FilePath)

    def PackageFiles(self,FilesList,Format="zip",Format2=""):
        if Format=="zip":
            with libarchive.file_writer(self.FilePath,Format) as Package:
              for Every in (FilesList):
                Package.add_files(Every)
        elif Format=="ustar" and Format2=="gzip":
            with libarchive.file_writer(self.FilePath,Format,Format2) as Package:
              for Every in (FilesList):
                Package.add_files(Every)