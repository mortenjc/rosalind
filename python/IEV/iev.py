import sys, re

sys.path.append('../common')
import toolbox as tb


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'


probs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

pop = lines[0].split(' ')

assert len(pop) == len(probs)
print(pop)

res = 0.0
for i in range(len(pop)):
    res += 2 * float(pop[i]) * probs[i]
print(res)
