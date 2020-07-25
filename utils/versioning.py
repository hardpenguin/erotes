import time

class Version(object):
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.number = None

    def read_from_file(self):
        f = open(self.file_path, "r")
        self.number = f.read()
        f.close()

    def generate_version(self, number):
        epoch_days = str(time.time()/60/60/24).split(".")[0]
        f = open(self.file_path, "w")
        self.number = "%s.%s" %(str(number), epoch_days)
        f.write(self.number)
        f.close()