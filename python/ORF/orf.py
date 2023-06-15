import sys
sys.path.append('../common')
import toolbox as tb


def proteinstring(sequence):
    state = 0 # 0 initial, 1 started, 2 stopped
    s = ''
    a = ''
    spc =''
    for i in range(0, len(sequence), 3):
        cod = sequence[i:i+3]
        if len(cod) != 3:
            break
        #print(f'i {i}, cod {cod}')
        if state == 0:
            if tb.is_start(cod):
                #print(f'{i} START')
                state = 1
                spc = " " * i
                s = tb.amino(cod)
                a += cod
                continue
            else:
                pass
                #print(f'ignore {cod}')
        elif state == 1:
                if tb.is_stop(cod):
                    state = 2
                    #print(f'{i} STOP')
                    break
                else:
                    #print(f'{i} {cod} {tb.amino(cod)}')
                    s += tb.amino(cod)
                    a += cod
        else:
            pass
            #print(f'state {state}')
    if state == 2:
        #print(f'{spc}{a}')
        return s
    else:
        return ''


# https://rosalind.info/problems/orf
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'

n, names, strings = tb.readfasta(filename)


def orf(sequence):
    res = set()
    for i in range(3):
        seq = sequence[i:]
        starts = tb.startpositions(seq)
        # if len(starts) == 0:
        #     continue
        for j in starts:
            tmp = proteinstring(seq[j:])
            if tmp != '':
                res.add(tmp)
    return res

orgsequence = strings[0]
res = orf(orgsequence)

# REVERSE COMPLEMENT
revsequence = tb.revcompl(orgsequence)
res = res | orf(revsequence)
for i in res:
    print(i)
