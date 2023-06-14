import sys

# https://rosalind.info/problems/iprb/

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

species = [ int(x) for x in lines[0].split(' ')]

k = float(species[0]) # AA
m = species[1] # A.
n = species[2] # ..
tot = sum(species)

p = k/tot * (k-1)/(tot-1) + k/tot * m/(tot-1)     + k/tot * n/(tot-1)
p+= m/tot * k/(tot-1)     + m/tot * (m-1)/(tot-1)*0.75 + m/tot * n/(tot-1)*0.5
p+= n/tot * k/(tot-1)     + n/tot * m/(tot-1) * 0.5

print(p)
