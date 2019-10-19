#!/usr/bin/env python3

import re
import sys

fasta_file=sys.argv[1]
sequence=""
with open(fasta_file) as fasta:
	for line in fasta:
		line=line.rstrip()
		match_object=re.search(r"(^>\S+)",line)
		if match_object:			
			if sequence:
				print(sequence)
				sequence=""
			print("ID: ",match_object.group(1),"\nDescription: ", sep="")
		else:
			sequence=sequence+line
	print(sequence)
#looking for Apol restriction site
	print("Liste des sites de restrictions d'Apol dans la sequence: ")
	for (s1,s2) in re.findall(r"([AG])(AATT[CT])",sequence):
		print(s1,"^",s2,sep="")
