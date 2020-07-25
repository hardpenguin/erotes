import os
import distutils.dir_util
import distutils.file_util

from utils import download_utils, directory_utils, archive, symlink_utils

def create_workplace(template_source, work_dir):
    template_name = template_source.split("/")[-1]
    workplace_path = "%s/workplace" % work_dir

    print("Creating workplace from [%s] template..." % template_name)
    distutils.dir_util.copy_tree(template_source,
                                workplace_path)

def download_love(link, platform, platform_path):
    package = download_utils.Downloadable(link["link"])
    destination = "%s/%s" % (platform_path, package.name)

    print("Downloading %s..." % package.name)
    package.download(destination)

    return(package.name) 

def unpack_love(package_name, platform, platform_path):
    package_basename = package_name
    for suffix in [".deb", ".zip"]:
        package_basename = package_basename.replace(suffix, "")

    target_path = "%s/%s" % (platform_path, package_basename)

    directory_utils.Folder(target_path).create()

    os.chdir(target_path)

    print("Unpacking %s..." % package_name)
    archive_path = "%s/%s" % (platform_path, package_name)
    archive.Archive(archive_path).unpack()

    if "linux" in platform:
        linux_archive_path = "%s/data.tar.xz" % target_path
        archive.Archive(linux_archive_path).unpack()

def copy_runtime(platform, source_path, platform_path):
    for root, dirs, files in os.walk(source_path):
        for f in files:
            current_file = "%s/%s" % (root, f)
            if "linux" in platform:
                if ("/usr/bin" in root) or ("/usr/lib" in root):
                    if os.path.islink(current_file):
                        symlink_path = platform_path+"/"+f
                        new_symlink = symlink_utils.Symlink(symlink_path)
                        new_symlink.create(current_file)
                    else:
                        distutils.file_util.copy_file(current_file,
                                                        platform_path)

            elif "windows" in platform:
                if ("love.exe" in files):
                    distutils.file_util.copy_file(current_file,
                                                    platform_path)
                

def start_project(config, work_dir):
    template = config["template"]
    template_path = "%s/templates/%s" % (work_dir,
                                        template)
    create_workplace(template_path, work_dir)

    for platform in config["platforms"]:
        downloads_path = "%s/downloads/%s" % (work_dir, platform)
        downloads_folder = directory_utils.Folder(downloads_path)
        downloads_folder.create()

        love_path = "%s/love/%s" % (work_dir, platform)
        love_folder = directory_utils.Folder(love_path)
        love_folder.Create()

        for link in config["links"]:
            os.chdir(work_dir)
            if link["platform"] == platform:
                file_downloaded = download_love(link,
                                                platform,
                                                downloads_path)
                unpack_love(file_downloaded,
                            platform,
                            downloads_path)
                copy_runtime(platform,
                            downloads_path,
                            love_path)

    print("Done.")