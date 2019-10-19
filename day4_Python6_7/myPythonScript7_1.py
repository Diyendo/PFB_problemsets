#!/usr/bin/env python3

import re

#n_line=0

with open("Python_07_nobody.txt","r") as nobody:
	for line in nobody:
#		line.rstrip()
#		n_line+=1
#		for match in re.finditer(r"Nobody", line):
		New_line=re.sub(r"Nobody","My Mama",line)	
		print(New_line)


			

#	found=re.search(r"Nobody",content)
#	print(content,found)
