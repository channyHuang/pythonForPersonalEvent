from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

for index in range(22, 42):
	file = '%d.mp3'%index; #file anme
	if not os.path.exists(file):
		print file;
		continue;
	else:
		print file;
	song = AudioSegment.from_mp3(file)
	words = split_on_silence(song, min_silence_len=2000, silence_thresh=-100)
	print file
	print len(words)

	j = 0;
	for i in words:
		j = j+1;
		new = AudioSegment.empty()
		new = i;
		new.export('%d/%03d.mp3'%(index,j), format='mp3')

