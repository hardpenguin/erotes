import time

class Version(object):
    
    def __init__(self, version_file_path):
        self.version_file_path = version_file_path

    def get_version(self):
        version_file = open(self.version_file_path, "r")
        version_number = version_file.read()
        version_file.close()
        return(version_number)

    def generate_version(self, version_number):
        epoch_days = str(time.time()/60/60/24).split(".")[0]
        version_file = open(self.version_file_path, "w")
        version_string = "%s.%s" %(str(version_number), epoch_days)
        version_file.write(version_string)
        version_file.close()
        return(self.get_version())