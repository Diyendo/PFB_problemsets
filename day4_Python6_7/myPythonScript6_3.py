#!/usr/bin/env python3

myPyt6_fq=[]
with open("Python_06.fastq","r") as Pyt6_fq : 
	for line in Pyt6_fq:
		line=line.rstrip()
		myPyt6_fq.append(line)

myPyt6_fq_str = ''.join(myPyt6_fq)

print("Number of lines in the fastq file is : ", len(myPyt6_fq),"\nNumber of characters is: ", len(myPyt6_fq_str), "\nThe average line length is: ", (len(myPyt6_fq_str)/len(myPyt6_fq)))
