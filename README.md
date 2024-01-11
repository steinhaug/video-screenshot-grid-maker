# Video Screenshot Grid Maker (VSGM)

Create a jpg file containing screenshots from a video presented in a grid.

<div class="show_none">

# Table of Contents

- [Video Screenshot Grid Maker (VSGM)](#video-screenshot-grid-maker-vsgm)
- [Table of Contents](#table-of-contents)
- [1. Prerequisites](#1-prerequisites)
  - [1.1 Requirements](#11-requirements)
  - [1.2 Installing FFmpeg](#12-installing-ffmpeg)
  - [1.2.1 Installing FFmpeg for windows](#121-installing-ffmpeg-for-windows)
  - [1.3 Installing the python FFmpeg wrapper](#13-installing-the-python-ffmpeg-wrapper)
- [2. Usage](#2-usage)
  - [2.1 How to use wizard](#21-how-to-use-wizard)
  - [2.2 Scan a specific folder](#22-scan-a-specific-folder)
  - [2.3 Example grid](#23-example-grid)
- [3. FAQ](#3-faq)
  - [3.1 Error in UnicodeEncode](#31-error-in-unicodeencode)
- [4. Version History](#4-version-history)
  - [4.1 Log](#41-log)
    - [v1.1](#v11)
    - [v1.0](#v10)
- [5. Information](#5-information)
  - [5.1 License](#51-license)
  - [5.2 Author](#52-author)

</div>

# 1. Prerequisites

## 1.1 Requirements

FFmpeg must be installed and accessible via the $PATH environment variable for VSGM to run. The python wrapper ffmpeg-python is also required.

## 1.2 Installing FFmpeg

Before using ffmpeg-python, FFmpeg must be installed and accessible via the $PATH environment variable.

There are a variety of ways to install FFmpeg, such as the [official download links](https://ffmpeg.org/download.html), or using your package manager of choice (e.g. sudo apt install ffmpeg on Debian/Ubuntu, brew install ffmpeg on OS X, etc.).

Regardless of how FFmpeg is installed, you can check if your environment path is set correctly by running the ffmpeg command from the terminal, in which case the version information should appear, as in the following example (truncated for brevity):

    $ ffmpeg
    ffmpeg version 4.2.4-1ubuntu0.1 Copyright (c) 2000-2020 the FFmpeg developers built with gcc 9 (Ubuntu 9.3.0-10ubuntu2)

Note: The actual version information displayed here may vary from one system to another; but if a message such as ffmpeg: command not found appears instead of the version information, FFmpeg is not properly installed.

## 1.2.1 Installing FFmpeg for windows

From the download page above you can select the [ffmpeg essentials build](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z), which contains the needed .exe files. Make sure they are available via the $PATH.

[ffmpeg-git-essentials.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z)

## 1.3 Installing the python FFmpeg wrapper

The latest version of ffmpeg-python can be acquired via a typical pip install:

    pip install ffmpeg-python

# 2. Usage

## 2.1 How to use wizard

Execute the vsgm.py file and it will ask you for a drive name, then you can select what folder to scan for video files.

    python vsgm.py

The script will scan the folder you chose and its subfolders for video files, and create screenshot grids with the same name.

## 2.2 Scan a specific folder

You can execute the script by adding the folder to scan for videos as a parameter.

    python vsgm.py e:\my-videos

## 2.3 Example grid

<img src="grid-example.jpg?v1.1" alt="grid example" width="850"></img>

# 3. FAQ

## 3.1 Error in UnicodeEncode

If you get an error dealing with UnicodeEncoding errors like:

    File "C:\Python311\Lib\encodings\cp1252.py", line 19, in encode  
    UnicodeEncodeError: 'charmap' codec can't encode character '\u0440' in position 59: character maps to <undefined>

Run the following command in terminal to make sure you are using UTF-8 which has all of the unicode characters.

    export PYTHONIOENCODING=utf-8  

# 4. Version History

## 4.1 Log

### v1.1 
    - Added videfilename and length in upper left corner  
    - Made the final image smaller if wider than 5000 px  
    - Added __init__py file in scripts folder  
    - Updated example image  

### v1.0
    - Project started  

# 5. Information

## 5.1 License

This project is licensed under the terms of the  [MIT](http://www.opensource.org/licenses/mit-license.php) License. Enjoy!

## 5.2 Author

Kim Steinhaug: [@steinhaug](http://twitter.com/steinhaug) [LinkedIn](https://no.linkedin.com/in/steinhaug) [Website](http://steinhaug.no/)
