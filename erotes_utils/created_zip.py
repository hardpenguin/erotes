import libarchive

class CreatedZip(object): # archive to be created
    
    def __init__(self,ContentsList,TargetPath):
        self.ContentsList=ContentsList
        self.TargetPath=TargetPath

    def PackageContents(self):
        with libarchive.file_writer(self.TargetPath+'/game.love', 'zip') as Archive:
          for Every in (self.ContentsList):
            Archive.add_files(Every)