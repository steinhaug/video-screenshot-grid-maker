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
  - [2.4 Cutting a video file](#24-cutting-a-video-file)
  - [2.5 Cropping a directory](#25-cropping-a-directory)
- [3. FAQ](#3-faq)
  - [3.1 Error in UnicodeEncode](#31-error-in-unicodeencode)
- [4. Version History](#4-version-history)
  - [4.1 Log](#41-log)
    - [v1.3](#v13)
    - [v1.2](#v12)
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


## 2.4 Cutting a video file

The following command will create two new video files from the given videofile, beginning from the start_time and length from there. First video
is 50 seconds, next video is 60 seconds.

    python ffmpeg-split.py -f "video_path" -m "json_file_path" -v libx264

    Json file:  
    [
        {
            "start_time": 1239,
            "length": 50,
            "rename_to": "video1-luxury.mkv"
        },
        {
            "start_time": 815,
            "length": 60,
            "rename_to": "video2-luxury.mkv"
        }
    ]

## 2.5 Cropping a directory

If you have a directory with images, say they all are 1920x1024. You would like to have them all be 720x512 as example, use the dir_crop.py.

    python dir_crop.py -i input_folder -x 720 -y 512

# 3. FAQ

## 3.1 Error in UnicodeEncode

If you get an error dealing with UnicodeEncoding errors like:

    File "C:\Python311\Lib\encodings\cp1252.py", line 19, in encode  
    UnicodeEncodeError: 'charmap' codec can't encode character '\u0440' in position 59: character maps to <undefined>

For windows systems, command prompt:

    set PYTHONIOENCODING=utf-8

PowerShell:

    $env:PYTHONIOENCODING = "utf-8"

Fow linux:

    export PYTHONIOENCODING=utf-8  

# 4. Version History

## 4.1 Log

### v1.3
    - Added tool: dir_crop.py, will crop all images in a directory
    - Added tool: ffmpeg-split.py, will cut parts from video files and save ito new video files

### v1.2
    - Added direct mode vsgm.py, "python vsgm.py [path]"
    - Bugfix: KeyError: 'width', ffmpeg.probe() function is not finding the width key in the first stream of the video file's metadata.

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

Kim Steinhaug, steinhaug at gmail dot com.

**Sosiale lenker:**
[LinkedIn](https://www.linkedin.com/in/steinhaug/), [SoundCloud](https://soundcloud.com/steinhaug), [Instagram](https://www.instagram.com/steinhaug), [Youtube](https://www.youtube.com/@kimsteinhaug), [X](https://x.com/steinhaug), [Ko-Fi](https://ko-fi.com/steinhaug), [Github](https://github.com/steinhaug), [Gitlab](https://gitlab.com/steinhaug)

**Generative AI lenker:**
[Udio](https://www.udio.com/creators/Steinhaug), [Suno](https://suno.com/@steinhaug), [Huggingface](https://huggingface.co/steinhaug)

**Resurser og hjelpesider:**
[Linktr.ee/steinhaugai](https://linktr.ee/steinhaugai), [Linktr.ee/stainhaug](https://linktr.ee/stainhaug), [pinterest/steinhaug](https://no.pinterest.com/steinhaug/), [pinterest/stainhaug](https://no.pinterest.com/stainhaug/)
