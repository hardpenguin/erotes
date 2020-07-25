import os

class Symlink(object):
    
    def __init__(self, path):
        self.path = path

    def create(self, symlink_to):
        link_to = os.readlink(symlink_to)
        if not os.path.exists(self.path):
            os.symlink(link_to, self.path)