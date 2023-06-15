import sys

# https://rosalind.info/problems/cons

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
datasets = -1
dataset = []
dsl = ''
for l in lines:
    if l[0] == '>':
        if datasets != -1:
            dataset.append(dsl)
            dsl = ''
        datasets += 1
    else:
        dsl += l
dataset.append(dsl)


stats = []
res = ""
for i in range(len(dataset[0])):
    cons = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}
    for j in range(len(dataset)):
        line = dataset[j]
        cons[line[i]] += 1
    stats.append(cons)
    max_key = max(cons, key=cons.get)
    res += max_key
print(res)

for base in ['A', 'C', 'G', 'T']:
    res = ''
    for i in range(len(dataset[0])):
        res += "{} ".format(stats[i][base])
    print(f'{base}: {res}')
