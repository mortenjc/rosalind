

# https://rosalind.info/problems/hamm/

# opening the file
file_obj = open("rosalind_hamm.txt", "r")

# reading the data from the file
file_data = file_obj.read()

# splitting the file data into lines
lines = file_data.splitlines()

dist = 0
for i in range(len(lines[0])):
    if lines[0][i] != lines[1][i]:
        dist += 1

print(f'hamming dist: {dist}')
