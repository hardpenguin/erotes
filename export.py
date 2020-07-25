import os
import libarchive
import distutils.file_util
import re

from utils import directory_utils, archive, symlink_utils, concatenation

def export_love(work_dir, name_str, version_str):
    denied = [
                ".git",
                ".gitignore"
            ]
    workplace_path = "%s/workplace" % work_dir
    os.chdir(workplace_path)

    l = os.listdir('.')
    for each in denied:
        if each in l:
            l.remove(each)

    export_path = "%s/export" % work_dir
    export_folder = directory_utils.Folder(export_path)
    export_folder.create()

    love_file_path = "%s/%s_%s.love" % (export_path, name_str, version_str)

    print("Creating .love file...")

    love_archive = archive.Archive(love_file_path)
    love_archive.package_files(l)

def export_platform(work_dir, name_str, version_str, platform):
    export_path = "%s/export/" % work_dir
    love_path = "%s/love/%s/" % (work_dir, platform)
    love_files = os.listdir(love_path)

    if "linux" in platform:
        love_binary = "love"
    elif "windows" in platform:
        love_binary = "love.exe"
    love_binary_path = "%s%s" % (export_path, love_binary)

    if "linux" in platform:
        game_binary = name_str
    elif "windows" in platform:
        game_binary = "%s.exe" % name_str
    game_binary_path = "%s%s" % (export_path, game_binary)

    love_file = "%s%s_%s.love" % (export_path, name_str, version_str)

    print("Creating %s export..." % platform)
    for each in love_files:
        current_file = "%s%s" % (love_path, each)
        if os.path.islink(current_file):
            symlink_path = "%s/%s" % (export_path, each)
            new_symlink = symlink_utils.Symlink(symlink_path)
            new_symlink.Create(current_file)
        else:
            love_subfile = "%s%s" % (love_path, each)
            distutils.file_util.copy_file(love_subfile,export_path)

    concatenated_binary = concatenation.Object(game_binary_path)
    concatenated_binary.concatenate(love_binary_path, love_file)

    if "linux" in platform:
        os.chmod(game_binary_path, 0o775)

    to_package = list(love_files)
    to_package.append(game_binary)
    to_remove = list(to_package)
    to_package.remove(love_binary)

    package_path = "%s/%s_%s_%s.zip" % (export_path,
                                        name_str,
                                        version_str,
                                        platform)

    os.chdir(export_path)
    export_package = archive.Archive(package_path)
    export_package.package_files(to_package)

    for each in to_remove:
        removed_file_path = "%s%s" % (export_path, each)
        os.remove(removed_file_path)    

def export_project(config, work_dir):
    print("Starting exports...")
    project_name = config.contents["name"]
    project_version = config.contents["version"]
    name_str = re.sub("[^0-9a-zA-Z]+", "_", project_name)
    name_str = name_str.lower()
    version_str = re.sub("[^0-9a-zA-Z]+", "_", project_version)
    platforms = config.contents["platforms"]
    export_love(work_dir, name_str, version_str)

    if "linux64" in platforms:
        export_platform(work_dir, name_str, version_str, "linux64")
    if "windows32" in platforms:
        export_platform(work_dir, name_str, version_str, "windows32")

    print("Done.")