# pyNfo
A simple Python Script for Windows that generates neat bbcode for your movie descriptions. Requires Python and Mediainfo CLI.

### Prerequisites
Right now this verson only works on Windows, sorry linux users, it won't take long to port a linux version. You will need the
included CLI Versionmediainfo.exe file or you grab the latest version from https://mediaarea.net/en/MediaInfo. Again make sure
that it's the CLI version. You will also need the imdb ID number (the numbers in the IMDb URL after the ```tt```)

### Installing
Download the files from the repsoitory and make sure that mediainfo.exe is in the same folder as pyNfo.py

### Running
Simply run ```pyNfo.py FILENAME.mp4 -i [IMDB id WTIHOUT tt]``` and it will generate a txt file formatted in bbcode with all the infromation necessary to make a description.

### Example

```
[font=courier new]
Scream 2 (1997)

[b]GENERAL:[/b]

Source....................: [color=#FF0000][b][/b][/color]
Movie Release.............: 12 Dec 1997
Genre.....................: Horror, Mystery
Size......................: 9.26 GiB
Runtime...................: 2:00:12 HH:MM:SS
Director..................: Wes Craven
Container.................: Matroska / mkv
IMDB......................: https://www.imdb.com/tt0120082

[b]VIDEO[/b]

Codec.....................: AVC
Type......................: 1080 p
Frame Rate................: 23.976 fps
Format Profile Level......: High@5.1
Bitrate...................: 8.982201 Mbps
Width x Height............: 1916 X 1080

[b]AUDIO[/b]

Codec.....................: DTS
Language..................: en
Channel(s)................: 6
Bitrate...................: 2 044 kbps
Sample Rate...............: 48.0kHz
Bit Depth.................: 16-bit

[b]NOTES[/b]

Bumped the brightness, contrast and the saturation a bit with Tweak.

[b]SCREENS:[/b]

Source on the LEFT Encode on the RIGHT
[/font]

[URL=http://www.imagebam.com/image/14a5701015949474][IMG]http://thumbs2.imagebam.com/e8/3c/2b/14a5701015949474.jpg[/IMG][/URL]           [URL=http://www.imagebam.com/image/a3f2101015950614][IMG]http://thumbs2.imagebam.com/6f/12/0d/a3f2101015950614.jpg[/IMG][/URL]

[URL=http://www.imagebam.com/image/8f7bb61015949544][IMG]http://thumbs2.imagebam.com/97/fd/05/8f7bb61015949544.jpg[/IMG][/URL]           [URL=http://www.imagebam.com/image/99c2681015950664][IMG]http://thumbs2.imagebam.com/c0/b8/da/99c2681015950664.jpg[/IMG][/URL]

[URL=http://www.imagebam.com/image/704ad31015949604][IMG]http://thumbs2.imagebam.com/c6/07/b0/704ad31015949604.jpg[/IMG][/URL]           [URL=http://www.imagebam.com/image/1d190f1015950734][IMG]http://thumbs2.imagebam.com/a7/b1/2b/1d190f1015950734.jpg[/IMG][/URL]

[URL=http://www.imagebam.com/image/21b0091015949654][IMG]http://thumbs2.imagebam.com/df/03/5d/21b0091015949654.jpg[/IMG][/URL]           [URL=http://www.imagebam.com/image/733d041015950784][IMG]http://thumbs2.imagebam.com/46/a4/6d/733d041015950784.jpg[/IMG][/URL]

[URL=http://www.imagebam.com/image/c208801015949674][IMG]http://thumbs2.imagebam.com/63/d8/0b/c208801015949674.jpg[/IMG][/URL]           [URL=http://www.imagebam.com/image/5423171015950854][IMG]http://thumbs2.imagebam.com/e5/f6/93/5423171015950854.jpg[/IMG][/URL]

[URL=http://www.imagebam.com/image/1fb35a1015949774][IMG]http://thumbs2.imagebam.com/c3/c1/b6/1fb35a1015949774.jpg[/IMG][/URL]           [URL=http://www.imagebam.com/image/9348fb1015950894][IMG]http://thumbs2.imagebam.com/16/fa/4e/9348fb1015950894.jpg[/IMG][/URL]```

### Result
The script will generate a .txt file formatted with movie information and technical information generated from both the IMDb api and
the mediainfo data. The name of the text file is taken from the title header of the media file and will appear in the same directory
that pyNfo is stored under.

### Post Instructions
The .txt file is forum ready and can be pasted and rendered properly on most trackers that allow bbcode. You will have to manually
add the source information as this can't be generated (yet!) along with screenshots that may be needed for some trackers. I do intended
to write a script that will use the imagebam api and incorporate it into this script.

Enjoy!
