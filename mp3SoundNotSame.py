from pydub import AudioSegment
import os

path = "../../Downloads/detector/"
songs = []
names = []
db = -100
for files in os.listdir(path):
	if os.path.isdir(files):
		continue;
	song = AudioSegment.from_mp3(path + files)
	songs.append(song)
	if song.dBFS > db:
		db = song.dBFS
	names.append(files)

i = 0
for song in songs:
	print names[i]
	song += abs(db - song.dBFS)
	song.export("./detector/" + names[i], format="mp3")
	i = i + 1
'''
file1 = "1.mp3"
file2 = "2.mp3"
targetFile = "3.mp3"
targetFile2 = "4.mp3"
song1 = AudioSegment.from_mp3(file1)
song2 = AudioSegment.from_mp3(file2)
dbplus = song1.dBFS - song2.dBFS
if dbplus < 0:
	song1 += abs(dbplus)
else:
	song2 += dbplus
song1.export(targetFile, format="mp3")
song2.export(targetFile2, format="mp3")
'''
