import sys

# https://rosalind.info/problems/orf

cod = { # M is start _ is stop
"TTT" : "F",  "CTT" : "L",  "ATT" : "I",  "GTT" : "V",
"TTC" : "F",  "CTC" : "L",  "ATC" : "I",  "GTC" : "V",
"TTA" : "L",      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA _      CAA Q      AAA K      GAA E
TAG _      CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA _      CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G
}

# opening the file
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'
file_obj = open(filename, "r")

# reading the data from the file
file_data = file_obj.read()

# splitting the file data into lines
lines = file_data.splitlines()
