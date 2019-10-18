#!/usr/bin/env python3

dna="GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG"

dna_upper = dna.upper()
nbrOfC = dna_upper.count("C")
nbrOfG = dna_upper.count("G")
nbrOfA = dna_upper.count("A")
nbrOfT = dna_upper.count("T")

print("There are:", "\n",nbrOfA, "A", "\n",nbrOfT, "T", "\n",nbrOfC, "C", "\n",nbrOfG, "G", "\nin the Dna sequence :", dna)

rna = dna_upper.replace("T","U")
print("the RNA equivalence of the DNA sequence is: ", rna)

ATcontent_str = "The AT content of the seauence is {}%."
AT_content = ((nbrOfA + nbrOfT) / len(dna_upper)) * 100
AT_content_prt = "{:.2f}".format(AT_content)
print(ATcontent_str.format(AT_content_prt))

GCcontent_str = "The GC content of the sequence is {}%."
GC_content = ((nbrOfG + nbrOfC) / len(dna_upper)) * 100
GC_content_prt = "{:.2f}".format(GC_content)
print(GCcontent_str.format(GC_content_prt))

sub_dna=dna_upper[99:200]
print("The substring from nucleotide number 100 to nucleotide number 200 of the DNA sequence is: ", "\n",sub_dna)

