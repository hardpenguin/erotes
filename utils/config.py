import json

class Config(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.contents = None
        self._read()

    def _read(self):
        with open(self.file_path, 'r') as file:
            self.contents = json.load(file)