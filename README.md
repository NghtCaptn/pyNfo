# pyNfo
A simple Python Script for Windows that generates neat bbcode for your movie descriptions. Requires Python and Mediainfo CLI.

### Prerequisites
Right now this verson only works on Windows, sorry linux users, it won't take long to port a linux version. You will need the
included CLI Versionmediainfo.exe file or you grab the latest version from https://mediaarea.net/en/MediaInfo. Again make sure
that it's the CLI version. You will also need the imdb ID number (the numbers in the IMDb URL after the ```tt```)

### Installing
Download the files from the repsoitory and make sure that mediainfo.exe is in the same folder as pyNfo.py

### Running
Simply ```python pyNfo.py``` in a cmd.exe and you will be prompted to enter the location of your media file. You can either drag
and drop the file into the command prompt and it will fill out the file location for you and add quotes ```" "``` if there are spaces.
You can also type in the file location if you want as well but make sure you add quotes otherwise you will get an exception.

### Example

```"Z:\Movie Title with Spaces.mp4"```

The next prompt you will get will ask you for the IMDb ID number WITHOUT the "tt". To find this, just go to IMDb and look up your movie
and copy/paste or type the numbers (only) into the prompt.

### Result
The script will generate a .txt file formatted with movie information and technical information generated from both the IMDb api and
the mediainfo data. The name of the text file is taken from the title header of the media file and will appear in the same directory
that pyNfo is stored under.

### Post Instructions
The .txt file is forum ready and can be pasted and rendered properly on most trackers that allow bbcode. You will have to manually
add the source information as this can't be generated (yet!) along with screenshots that may be needed for some trackers. I do intended
to write a script that will use the imagebam api and incorporate it into this script.

Enjoy!
