#!/usr/bin/env python3

import re
import sys

fasta_file=sys.argv[1]
sequence=""
with open(fasta_file) as fasta:
	for line in fasta:
		line=line.rstrip()
		match_object=re.search(r"(^>\S+)\s+(.+)",line)
		if match_object:			
			if sequence:
				print(sequence)
				sequence=""
			print("ID: ",match_object.group(1),"\nDescription: ", match_object.group(2), sep="")
		else:
			sequence=sequence+line
	print(sequence)
