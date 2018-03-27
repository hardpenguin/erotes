# Erotes

**Erotes** is a [LÖVE](http://love2d.org/) (love2d) project manager on Linux. It is meant to manage:

- creating an empty project template using chosen LÖVE version
- running the development version of the project
- exporting the project to .love file as well as Linux and Windows executable format

## Dependencies

- python2.7
- python-libarchive-c
- libarchive

On Ubuntu 16.04, these dependencies can be installed by running:

```sudo apt-get install python2.7 libarchive13 python-libarchive-c``` 

## Status

All basic functionalities listed in description are implemented.

## Todo

Including a lot of advice from code review by zolnierzfortuny - thanks!

- a release build (using pyinstaller)
- split erotes_start_project.DownloadAndUnpackLove() into two smaller functions: DownloadLove() and UnpackLove()
- create erotes_start_project.MoveUnpackedFiles() method that will walk the tree and copy files
- avoid naming methods after modules
- can we merge modules erotes_utils.created_zip and erotes_utils.unpacked_archive?
- local copy of templates and config in execution folder
- support for Windows and macOS development
- support for Linux, Windows and macOS export
- tests
- GUI (optional)