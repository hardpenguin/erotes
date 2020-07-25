import os
import sys
import distutils.dir_util
import distutils.file_util

from utils import versioning, directory_utils, archive

erotes_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(erotes_dir)

options = sys.argv[1:]
if len(options) < 1:
    print("Building in regular mode...")
    mode = "regular"
elif "--release" in options:
    print("Building in release mode...")
    mode = "release"
else:
    print("Unknown option!")
    sys.exit(0)

release_version = "1.2"
build_version = versioning.Version("version")
build_version.generate_version(release_version)

pyinstaller_executable = "pyinstaller"
pyinstaller_work_path = "./pyinstaller/build"
pyinstaller_dist_path = "./pyinstaller/dist"
spec_file = "erotes.spec"
pyinstaller_build_command = (
                                "%s "
                                "--workpath=\"%s\" "
                                "--distpath=\"%s\" "
                                "%s"
                            ) % (
                                    pyinstaller_executable,
                                    pyinstaller_work_path,
                                    pyinstaller_dist_path,
                                    spec_file
                                )

exe_path = "pyinstaller/dist/erotes"
distributable_path = "dist"

single_files = ["config.json"]
folders = ["templates"]

print("Building executable with pyinstaller...")
print(pyinstaller_build_command)
os.system(pyinstaller_build_command)

print("Creating distributable folder...")
distributable_folder = directory_utils.Folder(distributable_path)
distributable_folder.create()

print("Copying project executable...")
distutils.file_util.copy_file(exe_path, distributable_path)

print("Copying non-source files...")
for each in single_files:
    distutils.file_util.copy_file(each, distributable_path)    

for each in folders:
    destination_folder = "%s/%s" % (distributable_path, each)
    distutils.dir_util.copy_tree(each, destination_folder)

if mode == "release":
    print("Packaging distributable...")
    os.chdir(distributable_path)
    l = os.listdir(".")
    linux_dist_package_name = "%s/erotes-linux-%s.tar.gz" % (erotes_dir,
                                                        build_version.number)
    linux_dist_package = archive.Archive(linux_dist_package_name)
    linux_dist_package.package_files(l, "ustar", "gzip")

print("Done.")