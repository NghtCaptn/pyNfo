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
import argparse
import hashlib
import time
import glob
import uuid

'''
fileLocation = input("Enter File Location: ")
type(fileLocation)'''

def up(image):
    ts = round(time.mktime(time.localtime()))
    token = "nOGuYh64vNWDINwwev785NDNOW4cmkzI"
    secret = "Eyt1DCUkZbuA5V5P"
    sig3 = "CEGJ1W6HZCDE342KD7JE6GED2ZE9HKDSYSBZOHGOTT2WX3GB{}{}{}{}".format(ts, ts, token, secret).encode('utf-8')
    o = hashlib.md5()
    o.update(sig3)
    encode = o.hexdigest()
    fp = open(image, 'rb')
    file_data = fp.read()
    http = urllib3.PoolManager()
    api_key = "CEGJ1W6HZCDE342K"
    ad = str(uuid.uuid4().int)[:4]
    q = http.request('POST',
                     'http://www.imagebam.com/sys/API/resource/upload_image',
                     fields={'Content-Type': 'multipart/form-data',
                     'oauth_consumer_key': api_key,
                     'oauth_token': token,
                     'oauth_signature_method': 'MD5',
                     'oauth_signature': encode,
                     'oauth_timestamp': ts,
                     'oauth_nonce': ts,
                     'image': (os.path.basename(os.path.normpath(image)), file_data),
                     'content_type': 'family',
                     'thumb_size': '250x250'})
    h = json.loads(q.data)
    return '[url=' + str(h['rsp']['image']['URL']) + '][img]' + str(h['rsp']['image']['thumbnail'] + '[/img][/url]')

def single(fileLocation, n):
    i = 0
    j = 10
    n = int(n)
    y = 0
    ad = str(uuid.uuid4().int)[:4]
    for i in range(n):
        if j >= 60:
            j = j - 60
            y = 1
        screen = subprocess.check_call("ffmpeg -ss {4}:{3}:00 -t 1 -i \"{0}\" -vframes 1 \"{5}-frame-{2}-{1}.png\"".format(fileLocation, ad, i, j, y, mTitle))
        i += 1
        j += 5

parser = argparse.ArgumentParser(prog='pyNfo.py', description='Script that reads and generates media and IMDb info of a video file', usage='%(prog)s [FILENAME] [options]')
parser.add_argument('location', metavar='Full Path To File', help='File Location')
parser.add_argument('-i', help='IMDB id WTIHOUT TT', required=True)
parser.add_argument('-n', help='NUMBER OF SCREEN SHOTS', required=True)
args = parser.parse_args()
fileLocation = args.location
imdbId = args.i
n = args.n
mediaCommand = subprocess.check_call("mediainfo.exe --output=JSON --LogFile=data.json \"{0}\"".format(fileLocation), shell=True)

with open('data.json', 'r') as f:
	mediaNfo = json.load(f)
	#print(mediaNfo)
'''imdbId = input("Enter IMDb move ID: ")
type(imdbId)'''
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
file.write("Source....................: [color=#FF0000][b][/b][/color]")
file.write("\n")
file.write("Movie Release.............: %s" % data['Released'])
file.write("\n")
file.write("Genre.....................: %s" % data['Genre'])
file.write("\n")
fSize1 = int(mediaNfo['media']['track'][0]['FileSize']) / 1024
fSize2 = fSize1 / 1024
fSize = fSize2 / 1024
file.write("Size......................: %.2f GiB" % fSize)
file.write("\n")
intTime = int(float(mediaNfo['media']['track'][0]['Duration']))
runTime = str(datetime.timedelta(seconds=intTime))
file.write("Runtime...................: %s HH:MM:SS" % runTime)
file.write("\n")
file.write("Director..................: %s" % data['Director'])
file.write("\n")
file.write("Container.................: %s / %s" % (mediaNfo['media']['track'][0]['Format'], mediaNfo['media']['track'][0]['FileExtension']))
file.write("\n")
file.write("IMDB......................: https://www.imdb.com/title/tt%s" % imdbId)
file.write("\n")
file.write("\n")
file.write("[b]VIDEO[/b]")
file.write("\n")
file.write("\n")
file.write("Codec.....................: %s" % mediaNfo['media']['track'][1]['Format'])
file.write("\n")
file.write("Type......................: %s p" % mediaNfo['media']['track'][1]['Height'])
file.write("\n")
file.write("Frame Rate................: %s fps" % mediaNfo['media']['track'][1]['FrameRate'])
file.write("\n")
file.write("Format Profile Level......: %s@%s" % (mediaNfo['media']['track'][1]['Format_Profile'], mediaNfo['media']['track'][1]['Format_Level']))
file.write("\n")
bitRate = int(mediaNfo['media']['track'][1]['BitRate']) / 1000000
file.write("Bitrate...................: %s Mbps" % bitRate)
file.write("\n")
file.write("Width x Height............: %s X %s" % (mediaNfo['media']['track'][1]['Width'], mediaNfo['media']['track'][1]['Height']))
file.write("\n")
file.write("\n")
file.write("[b]AUDIO[/b]")
file.write("\n")
file.write("\n")
file.write("Codec.....................: %s" % mediaNfo['media']['track'][2]['Format'])
file.write("\n")
if mediaNfo['media']['track'][2]['Language'] == "en":
	lang = "English"
file.write("Language..................: {0}".format(lang))
file.write("\n")
file.write("Channel(s)................: %s" % mediaNfo['media']['track'][2]['Channels'])
file.write("\n")
aBrate = round(int(mediaNfo['media']['track'][2]['BitRate']) / 1000)
file.write("Bitrate...................: %s Kbps" % aBrate)
file.write("\n")
smplRate = int(mediaNfo['media']['track'][2]['SamplingRate']) / 1000
file.write("Sample Rate...............: %skHz" % smplRate)
file.write("\n")
format = mediaNfo['media']['track'][2]['Format']
if format in 'AAC':
	file.write("Bit Depth.................: 16-bit")
if format in 'DTS':
	file.write("Bit Depth.................: %s-bit" % mediaNfo['media']['track'][2]['BitDepth']) 
file.write("\n")
file.write("\n")
file.write("[b]SCREENS:[/b]")
file.write("[/font]")
file.write("\n")
file.write("\n")
mTitle = mediaNfo['media']['track'][0]['Title']
single(fileLocation, n)
a = []
path = os.getcwd()
b = []
for filename in glob.glob(os.path.join(path, '*.png')):
	a.append(filename)
for l in range(len(a)):
	b.append(up(a[l]))
	print("Image {0} Uploaded.".format(a[l]))
sCount = 0
for v in range(len(b)):
	file.write(b[v])
	sCount = sCount + 1
	if sCount == 4:
		file.write('\n')
		sCount = 0


print("File Saved to: %s.txt" % mediaNfo['media']['track'][0]['Title'])
os.remove('data.json')
for rm in range(len(a)):
	os.remove(a[rm])