#!/usr/bin/env python3

taxa="sapiens, erectus, neanderthalensis"

print("the content of the varaible taxa is: ", taxa)

print("taxa[1] is: ", taxa[1])

print("The type of the variable taxa is: ", type(taxa))

species=taxa.split(", ")
print("the content of the variable species is: ", species)

print("species[1] is: ", species[1])

print("the type of the variable species is: ", type(species))

species_sorted=sorted(species)
print("The sorted list species is: ", species_sorted)

species_sorted_len=sorted(species, key=len)
print("The sorted list species by length of elements is: ", species_sorted_len)
