# pyNfo
A simple Python Script for Windows that generates neat bbcode for your movie descriptions. Requires Python and Mediainfo CLI.

# Update 11/5/2018
The script now uses ffmpeg to generate screen shots of a video file, uploads it to imagebam then generates the correct bbcode for thumbnail links to the images. Upon completeion of the script the image files are deleted from host computer. As pyNfo uploads to imagebam it displays out the full path of each file location upon successful completion. I also fix the language field so it displays "English" as opposed to "en". The URL for the imdb info is also fixed.

### Prerequisites
Right now this verson only works on Windows, sorry linux users, it won't take long to port a linux version. You will need the
included CLI Versionmediainfo.exe file or you grab the latest version from https://mediaarea.net/en/MediaInfo. Again make sure
that it's the CLI version. You will also need the imdb ID number (the numbers in the IMDb URL after the ```tt```)

### Installing
Download the files from the repsoitory and make sure that mediainfo.exe is in the same folder as pyNfo.py

### Running
Simply run ```pyNfo.py FILENAME.mp4 -i [IMDB id WTIHOUT tt] -n [NUMBER OF SCREEN SHOTS YOU WANT GENERATED]``` and it will generate a txt file formatted using bbcode, screenshots and upload them to imagebam and adding the bbcoded thumbnail links to the txt file. MAKE SURE you do not have ANY OTHER .png files WITHIN the FOLDER that the script is running in otherwise it will PROCESS the extra .png files into your txt file and DELETE them all as well.

### Result
The script will generate a .txt file formatted with movie information and technical information generated from both the IMDb api and
the mediainfo data. The name of the text file is taken from the title header of the media file and will appear in the same directory
that pyNfo is stored under.

### Post Instructions
The .txt file is forum ready and can be pasted and rendered properly on most trackers that allow bbcode. You will have to manually
add the source information as this can't be generated (yet!) along with screenshots that may be needed for some trackers. I do intended
to write a script that will use the imagebam api and incorporate it into this script.

Enjoy!

### Example

```[font=courier new]
Crazy Six (1997)

[b]GENERAL:[/b]

Source....................: [color=#FF0000][b][/b][/color]
Movie Release.............: 01 Nov 1997
Genre.....................: Action, Crime
Size......................: 14.19 GiB
Runtime...................: 1:34:55 HH:MM:SS
Director..................: Albert Pyun
Container.................: Matroska / mkv
IMDB......................: https://www.imdb.com/tt0118897

[b]VIDEO[/b]

Codec.....................: AVC
Type......................: 1080 p
Frame Rate................: 23.976 fps
Format Profile Level......: High@4.1
Bitrate...................: 19.998746 Mbps
Width x Height............: 1920 X 1080

[b]AUDIO[/b]

Codec.....................: FLAC
Language..................: en
Channel(s)................: 2
Bitrate...................: 1392
Sample Rate...............: 48.0kHz


[b]SCREENS:[/b][/font]

[url=http://www.imagebam.com/][img]http://imagebam.com/[/img][/url]

```
