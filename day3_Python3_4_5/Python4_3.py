#!/usr/bin/env python3

import sys

x=int(sys.argv[1])

nbr=1
fact_x=x

while nbr < x: 
	fact_x=fact_x*(x-nbr)
	nbr+=1
print(x,"! = ",fact_x,sep="")
