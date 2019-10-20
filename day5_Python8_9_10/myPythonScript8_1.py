#!/usr/bin/env python3

import re
import sys

fasta_file=sys.argv[1]
sequence_list=[]
sequence=""
seqName_list=[]
seqName=""
fasta_dict={}
n=0

with open(fasta_file) as fasta:
	for line in fasta:
		line=line.rstrip()
		found=re.search(r"(^>\S+)\s+(.+)",line) #Found all the header and assign them to found	
		if found:																#If the line is a header	
			seqName=found.group(1) 								#Assign the ID in a variable seqName
			seqName=seqName.replace(">","")				#Remove the ">" at the beginning of the ID
			seqName_list.append(seqName)					#Store the IDs in a list called seqName_list
			if sequence:														
				sequence=sequence.upper()						#Convert the sequence to upper case
				sequence_list.append(sequence)			#Store the sequences in a list calles sequence_list
				sequence=""
		else:
			sequence=sequence+line								#Concatenate successive lines of sequences in a variable called sequence

sequence_list.append(sequence) 							#Append the last sequence to the end of the sequence_list 

for name in seqName_list:												
	fasta_dict[name]={}												#open fasta_dict and assign the first key to the first name in seqName, and the value is a dictionary	
	fasta_dict[name]["count_A"]=sequence_list[n].count("A") #add a dictionary with the key as the nt_count and its value
	fasta_dict[name]["count_T"]=sequence_list[n].count("T")
	fasta_dict[name]["count_C"]=sequence_list[n].count("C")
	fasta_dict[name]["count_G"]=sequence_list[n].count("G")
	n+=1



for gene in fasta_dict:
	count=fasta_dict[gene]	
	print("ID is:",gene,"\tCount of A:",count["count_A"],"\tCount of T:",count["count_T"],"\tCount of C:",count["count_C"],"\tCount of G:",count["count_G"])
