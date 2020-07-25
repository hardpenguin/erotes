import datetime

class Version(object):
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.number = None
        self._read_from_file()

    def _read_from_file(self):
        f = open(self.file_path, "r")
        self.number = f.read()
        f.close()

    def generate_version(self, number):
        date_now = datetime.datetime.utcnow()
        date_epoch = datetime.datetime(1970,1,1)
        date_diff = date_now - date_epoch
        epoch_days = str(date_diff.days)
        
        f = open(self.file_path, "w")
        self.number = "%s.%s" %(str(number), epoch_days)
        f.write(self.number)
        f.close()