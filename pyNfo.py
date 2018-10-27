'''
MIT License

Copyright (c) 2018 NghtCaptn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import json
import requests
import urllib3
import sys, string, os, subprocess
import random
import datetime

fileLocation = input("Enter File Location: ")
type(fileLocation)
mediaCommand = subprocess.check_call("mediainfo.exe --output=JSON --LogFile=data.json %s" % fileLocation, shell=True)

with open('data.json', 'r') as f:
	mediaNfo = json.load(f)
	#print(mediaNfo)
imdbId = input("Enter IMDb move ID: ")
type(imdbId)
http = urllib3.PoolManager()
url = "http://www.omdbapi.com/?apikey=b8272f7d&i=tt%s" % imdbId
r = http.request('GET', '%s' % url)
data = json.loads(r.data.decode('utf-8'))
file = open('%s.txt' % mediaNfo['media']['track'][0]['Title'], 'w')
file.write("[font=courier new]")
file.write("\n")
file.write("%s" % mediaNfo['media']['track'][0]['Title'])
file.write("\n")
file.write("\n")
file.write("[b]GENERAL:[/b]")
file.write("\n")
file.write("\n")
file.write("Source......................................: [color=#FF0000][b][/b][/color]")
file.write("\n")
file.write("Movie Release...............................: %s" % data['Released'])
file.write("\n")
file.write("Genre.......................................: %s" % data['Genre'])
file.write("\n")
fSize1 = int(mediaNfo['media']['track'][0]['FileSize']) / 1024
fSize2 = fSize1 / 1024
fSize = fSize2 / 1024
file.write("Size........................................: %.2f GiB" % fSize)
file.write("\n")
intTime = int(float(mediaNfo['media']['track'][0]['Duration']))
runTime = str(datetime.timedelta(seconds=intTime))
file.write("Runtime.....................................: %s HH:MM:SS" % runTime)
file.write("\n")
file.write("Director....................................: %s" % data['Director'])
file.write("\n")
file.write("Container...................................: %s / %s" % (mediaNfo['media']['track'][0]['Format'], mediaNfo['media']['track'][0]['FileExtension']))
file.write("\n")
file.write("IMDB........................................: https://www.imdb.com/tt%s" % imdbId)
file.write("\n")
file.write("\n")
file.write("[b]VIDEO[/b]")
file.write("\n")
file.write("\n")
file.write("Codec.......................................: %s" % mediaNfo['media']['track'][1]['Format'])
file.write("\n")
file.write("Type........................................: %s p" % mediaNfo['media']['track'][1]['Height'])
file.write("\n")
file.write("Frame Rate..................................: %s fps" % mediaNfo['media']['track'][1]['FrameRate'])
file.write("\n")
file.write("Format Profile Level........................: %s@%s" % (mediaNfo['media']['track'][1]['Format_Profile'], mediaNfo['media']['track'][1]['Format_Level']))
file.write("\n")
bitRate = int(mediaNfo['media']['track'][1]['BitRate']) / 1000000
file.write("Bitrate.....................................: %s Mbps" % bitRate)
file.write("\n")
file.write("Width x Height..............................: %s X %s" % (mediaNfo['media']['track'][1]['Width'], mediaNfo['media']['track'][1]['Height']))
file.write("\n")
file.write("\n")
file.write("[b]AUDIO[/b]")
file.write("\n")
file.write("\n")
file.write("Codec.......................................: %s" % mediaNfo['media']['track'][2]['Format'])
file.write("\n")
file.write("Language....................................: %s" % mediaNfo['media']['track'][2]['Language'])
file.write("\n")
file.write("Channel(s)..................................: %s" % mediaNfo['media']['track'][2]['Channels'])
file.write("\n")
smplRate = int(mediaNfo['media']['track'][2]['SamplingRate']) / 1000
file.write("Sample Rate.................................: %skHz" % smplRate)
file.write("\n")
file.write("Bit Depth...................................: %s-bit" % mediaNfo['media']['track'][2]['BitDepth'])
file.write("\n")
file.write("\n")
file.write("[b]Screens:[/b]")
file.write("\n")
file.write("\n")
file.write("<-------------------------------------------: PUT SCREENS BBCODE HERE!")
file.write("[/font]")
print("File Saved to: %s.txt" % mediaNfo['media']['track'][0]['Title'])
print(smplRate)
os.remove('data.json')