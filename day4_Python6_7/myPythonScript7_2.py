#!/usr/bin/env python3

import re

with open("Python_07.fasta") as Pyt1_fa:
	for line in Pyt1_fa:
		line=line.rstrip()
		match_object=re.search(r"(^>\S+)\s+(.+)",line)
		if match_object:
			print("ID: ",match_object.group(1),"\nDescription: ", match_object.group(2), sep="")

