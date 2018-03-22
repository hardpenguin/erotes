import os

class CreatedFolder(object): # folder to be created, needs name

    def __init__(self,Path):
        self.Path=Path

    def Create(self): # creates folder with a object defined name in a specified path
        if not os.path.exists(self.Path):
            os.makedirs(self.Path)
        return(self.Path)
