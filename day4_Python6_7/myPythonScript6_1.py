#!/usr/bin/env python3

with open("/Users/info/PFB_problemsets/day4_Python6_7/Python_06.txt","r") as Pyt06_txt, open("/Users/info/PFB_problemsets/day4_Python6_7/Python_06_uc.txt","w") as Pyt_06_upper:
	for line in Pyt06_txt:
		line=line.rstrip()
		line_upper = line.upper()
		Pyt_06_upper.write(line_upper + "\n")
		print(line_upper)
	print("Wrote 'Pyt_06_uc.txt'")


