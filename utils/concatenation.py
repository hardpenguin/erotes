import os

class Object(object):
    
    def __init__(self, file_path):
        self.file_path = file_path

    def concatenate(self, input1, input2):
        with open(self.file_path, "wb") as out_file:
            for part in [input1, input2]:
                with open(part, "rb") as in_file:
                    in_file_contents = in_file.read()
                    out_file.write(in_file_contents)
                in_file.close()
        out_file.close()
