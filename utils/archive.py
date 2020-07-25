import libarchive

class Archive(object):
    
    def __init__(self, file_path):
        self.file_path = file_path

    def unpack(self):
        libarchive.extract_file(self.file_path)

    def package_files(self,
                    files_list,
                    archive_format="zip",
                    archive_format2=""):
        if archive_format == "zip":
            with libarchive.file_writer(self.file_path,
                                        archive_format) as package:
                for every in (files_list):
                    package.add_files(every)
        elif (archive_format == "ustar" and 
                archive_format2 == "gzip"):
            with libarchive.file_writer(self.file_path,
                                        archive_format,
                                        archive_format2) as package:
                for every in (files_list):
                    package.add_files(every)