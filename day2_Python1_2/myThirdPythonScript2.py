#!/usr/bin/env python3

import sys

x = sys.argv[1]
x1 = float(x)

print("The number tested is",x)

if x1 == 0:
	print("the number is 0")
else:
	if ((x1/2)-(x1//2))  == 0:
		print(x, "is an even number")
	else:
		print(x, "is an odd number")
	if x1 > 0:
		if x1 < 50:
			print(x,"is positive and lesser than 50")
		elif ((x1/3)-(x1//3)) == 0:
			print(x, "is positive, greater than 50 and divisible by 3")
		elif x1 == 50:
			print("50 equal 50")
		else:
			print(x, "is positive and greater than 50")
	else:
		print(x,"is negative")
