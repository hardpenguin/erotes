import libarchive

class Archive(object): # archive to be unpacked
    
    def __init__(self, file_path):
        self.file_path = file_path

    def unpack(self):
        libarchive.extract_file(self.file_path)

    def package_files(self,
                    files_list,
                    format="zip",
                    format2=""):
        if format == "zip":
            with libarchive.file_writer(self.file_path, format) as package:
              for every in (files_list):
                package.add_files(every)
        elif format == "ustar" and format2 == "gzip":
            with libarchive.file_writer(self.file_path,
                                        format,
                                        format2) as package:
              for every in (files_list):
                package.add_files(every)