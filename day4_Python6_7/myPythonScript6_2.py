#!/usr/bin/env python3

Pyt6_lib={}
Pyt6_lib_comp={}


with open("Python_06.seq.txt","r") as Pyt6_seq:
	for line in Pyt6_seq:
		seqRev="" #in order to have the variable returning empty at each iteration
		line=line.rstrip()
		seqName,seq = line.split("\t")
		Pyt6_lib[seqName] = seq
		seqNameComp = ">"+seqName+" Reverse complement"
		for nt in seq:
			nt = nt.upper()
			if nt == "A":
				rev_nt=nt.replace("A","T")
			elif nt == "T":
				rev_nt=nt.replace("T","A")
			elif nt == "C":
				rev_nt=nt.replace("C","G")
			elif nt == "G":
				rev_nt=nt.replace("G","C")
			else:
				rev_nt=nt
			
			seqRev=seqRev+rev_nt
		Pyt6_lib_comp[seqNameComp]=seqRev


#print(Pyt6_lib)
#print(Pyt6_lib_comp)

for seqName in Pyt6_lib_comp:
	print(seqName, "\n",Pyt6_lib_comp[seqName], sep="") #print and redirect in a file with ">"


#x="ATCGAAAa"
#rev_x=""

#for nt in x:
#	nt = nt.upper()
#	if nt == "A":
#		rev_nt=nt.replace("A","T")
#	elif nt == "T":
#		rev_nt=nt.replace("T","A")
#	elif nt == "C":
#		rev_nt=nt.replace("C","G")
#	elif nt == "G":
#		rev_nt=nt.replace("G","C")
#	else:
#		rev_nt=nt
#	print(rev_nt)
#	rev_x=rev_x+rev_nt
#print(rev_x)
