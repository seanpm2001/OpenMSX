#! /usr/bin/env python

import string
import sys
import subprocess
import os

while 1:
    data = sys.stdin.readline()
    if data != '':
	# leave out all comment lines (lines starting with '#')
	comment_pos = string.find(data,'#')
	if comment_pos == 0:
		continue
	# separate the single entries by ';'
	separate = string.split(data,";")
	if len(separate) != 4:
		continue
	systemtype = (os.uname())[0]
	if systemtype == 'Linux':
		md5call = ["md5sum"]
	elif systemtype == 'Darwin':
		md5call = ["md5", "-5"]
	else:
		md5call = ["md5sum"]
	md5call = md5call + ["src/"+string.strip(separate[1])]
	md5sum = subprocess.Popen(md5call, stdout=subprocess.PIPE).communicate()[0]
	md5sum = string.split(md5sum)
	res = separate[1] + "\t= " + md5sum[0] + "\n"
        sys.stdout.write(res)
    else:
        sys.stdout.flush()
        break
