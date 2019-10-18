#!/usr/bin/env python3

import sys

#script1
#for nbr in range(1,101):
#	print(nbr)

#script2
#my_list=[nbr for nbr in range(1,101)]
#print(my_list)

#script3
#x=int(sys.argv[1])
#y=int(sys.argv[2])

#my_list=[nbr for nbr in range(x,(y+1))]
#print("The number from",x,"to",y,"are: ",my_list)

#script4
x=int(sys.argv[1])
y=int(sys.argv[2])

my_list=[nbr for nbr in range(x,(y+1))]
my_list2=[]
for nbr in my_list:
	if nbr%2 != 0:
		my_list2.append(nbr)
print("The odd numbers from",x,"to",y,"are: ",my_list2)
