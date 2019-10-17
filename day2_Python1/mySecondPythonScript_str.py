#!/usr/bin/env python3

import sys

dna = "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"
codon=sys.argv[1]
if codon in dna :
	print(codon,"is in",dna)
else :	
	print(codon,"is not in",dna)
