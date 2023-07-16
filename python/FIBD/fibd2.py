import sys
sys.path.append('../common')
import toolbox as tb
import files as f

# https://rosalind.info/problems/fibd

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

assert len(lines) == 1

n, d = lines[0].split(' ')
n = int(n)
d = int(d)

print(n,d)



def rabbits(n, d):
    imat = [0] * n
    matu = [0] * n
    dead = [0] * n

    imat[0] = 1
    matu[0] = 0

    imat[1] = 0
    matu[1] = 1
    for i in range(2, n):
        if i-d <= 0:
            dead[i] = 0
        else:
            dead[i] = matu[i-d]
        imat[i] = matu[i-1]
        matu[i] = matu[i-1] + imat[i-1] - dead[i]

    for i in range(n):
        print(f'gen {i+1}: {imat[i]+matu[i]-dead[i]} - mature {matu[i]}, immature {imat[i]}, deaths {dead[i]}')
    print()
    return imat[n-1]+matu[n-1]-dead[n-1]
#rabbits(n, d)
print('-----')
rabbits(7,4) # 9
rabbits(7,5) # 11
rabbits(12,3) # 21
rabbits(25,31) # 75025
rabbits(30,30) # 832040
rabbits(35, 29) # 9227437
