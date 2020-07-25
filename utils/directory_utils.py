import os

class Folder(object):

    def __init__(self, path):
        self.path = path

    def create(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
