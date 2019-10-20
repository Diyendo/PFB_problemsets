#!/usr/bin/env python3

import sys
import re

fasta_file=sys.argv[1]
sequence_list=[]
sequence_comp_list=[]
sequence=""
sequence_comp=""
seqName_list=[]
seqName=""
fasta_dict={}
n=0
condons=""
codon_list1=[]
codon_list2=[]
codon_list3=[]
codon_list1_comp=[]
codon_list2_comp=[]
codon_list3_comp=[]

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

for seq in sequence_list:
	sequence_comp=seq[::-1]
	sequence_comp=sequence_comp.replace("T","A")
	sequence_comp=sequence_comp.replace("a","T")
	sequence_comp=sequence_comp.replace("C","c")
	sequence_comp=sequence_comp.replace("G","C")
	sequence_comp=sequence_comp.replace("c","G")
	sequence_comp_list.append(sequence_comp)

for seq in sequence_list:
	codons= re.findall(r"(.{3})", seq)				#Find all the codons in the sequences store in sequence_list
	codon_list1.append(codons)								#Appen in a list codons, the list of codons
for seq in sequence_list:
	codons= re.findall(r"(.{3})", seq[1:]) 	#Find all the codons of the frame 2, starting at the 2nd nt
	codon_list2.append(codons)
for seq in sequence_list:
	codons= re.findall(r"(.{3})", seq[2:])
	codon_list3.append(codons)							#Find all the codons of the frame 3, starting at the 3rd nt

for seq_comp in sequence_comp_list:
	codons= re.findall(r"(.{3})", seq_comp)
	codon_list1_comp.append(codons)
for seq_com in sequence_comp_list:
	codons= re.findall(r"(.{3})", seq_comp[1:])
	codon_list2_comp.append(codons)
for seq_com in sequence_comp_list:
	codons= re.findall(r"(.{3})", seq_comp[2:])
	codon_list3_comp.append(codons)

for name in seqName_list:												
	fasta_dict[name]={}												#open fasta_dict and assign the first key to the first name in seqName, and the value is a dictionary	
	fasta_dict[name]["count_A"]=sequence_list[n].count("A") #add a dictionary with the key as the nt_count and its value
	fasta_dict[name]["count_T"]=sequence_list[n].count("T")
	fasta_dict[name]["count_C"]=sequence_list[n].count("C")
	fasta_dict[name]["count_G"]=sequence_list[n].count("G")
	fasta_dict[name]["codons1"]=codon_list1[n]
	fasta_dict[name]["codons2"]=codon_list2[n]
	fasta_dict[name]["codons3"]=codon_list3[n]
	fasta_dict[name]["codons1_comp"]=codon_list1_comp[n]
	fasta_dict[name]["codons2_comp"]=codon_list2_comp[n]
	fasta_dict[name]["codons3_comp"]=codon_list3_comp[n]
	n+=1

for gene in fasta_dict:
	count=fasta_dict[gene]	
	print(gene,"-frame-1-codons")
	print(count["codons1"])
	print(gene,"complementary-frame-1-codons")
	print(count["codons1_comp"])
	print(gene,"-frame-2-codons")
	print(count["codons2"])
	print(gene,"complementary-frame-2-codons")
	print(count["codons2_comp"])
	print(gene,"-frame-3-codons")
	print(count["codons3"])
	print(gene,"complementary-frame-3-codons")
	print(count["codons3_comp"])
