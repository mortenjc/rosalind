import sys

# https://rosalind.info/problems/subs/

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

string = lines[0]
patt = lines[1]

i = 0
while True:
    substr = string[i:]
    p = string[i:].find(patt)
    if p == -1:
        break
    i = i + p + 1
    print(i)
