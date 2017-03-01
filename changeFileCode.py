import codecs
import os
import glob
import sys
import chardet

#coding=utf-8
print sys.getdefaultencoding()


def changeTxtFile():
	path = 'D:/useAsE/mycode/python/201611BBC';
	filenames = glob.glob(path+'/*.txt');
	print len(filenames)

	for filename in filenames:
		adchar=chardet.detect(filename)
		#print adchar['encoding']

		out = open(filename, "r");
		try:
			lists = out.readlines();
		finally:
			out.close();
		out = file(filename, "w");	
		for item in lists:
			out.write(item.decode('utf-8').encode('utf-8'));
		out.close();	

changeTxtFile();	
