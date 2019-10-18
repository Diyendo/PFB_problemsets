#!/usr/bin/env python3

my_list = [101,2,15,22,95,33,2,27,72,15,52]
for elt in my_list:
	if elt%2 == 0:
		print(elt)

my_list_sorted = sorted(my_list)

even_sum=0
odd_sum=0

for elt in my_list_sorted : 
	print(elt)
	if elt%2 ==0:
		even_sum=even_sum+elt
	else:
		odd_sum=odd_sum+elt
print("The even values cumulative sum is: ",even_sum,"\nThe odd values cumulative sum is: ",odd_sum)
