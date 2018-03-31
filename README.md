# Erotes

**Erotes** is a [LÖVE](http://love2d.org/) (love2d) project manager on Linux. It is meant to manage:

- creating an empty project template using chosen LÖVE version
- running the development version of the project
- exporting the project to .love file as well as Linux and Windows executable format

## Usage

```
Syntax:
 erotes [options]

Available options:
  -s,    --start               starts the new project                  
  -r,    --run                 runs the project currently in development
  -e,    --export              exports the currently developed project 
```


## Dependencies

- python2.7
- python-libarchive-c
- libarchive

On Ubuntu 16.04, these dependencies can be installed by running:

```sudo apt-get install python2.7 libarchive13 python-libarchive-c```

To build the project you also need [pyinstaller](https://www.pyinstaller.org/). It has to be installed using pip:

```pip install pyinstaller```

## Building

Run:

```./build.py``` 

## Status

Starting and running the project is already implemented. Export is limited to .love file for now.

## Todo

- bundle libarchive with the erotes pyinstaller build
- support for Windows and macOS development
- support for Linux, Windows and macOS export
- naming and versioning LÖVE project
- Linux LÖVE dependencies
- tests
- GUI (optional)