# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:24:56 2016

@author: admin
"""

d = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}

def readdata(location):
    with open(location) as f:
        m = float(f.readline()[:-1])
        ions = []
        for i in f:
            ions.append(float(i[:-1]))
    return m, ions



def infer_peptide(current, remain, d):

    for i in remain:
        for j in d:
            if abs(d[j] - (i-current)) < 0.001:
                #print d[j], i, current
                return j
    return -1

def all_seq(ions, d):
    n = (len(ions)-2)/2

    res = ''
    current = ions[0]
    remain = ions[1:]

    while len(res) < n:
        temp = infer_peptide(current, remain, d)
        if temp == -1:
            return res
        else:
            res += temp
            current += d[temp]
            #print str(remain) + 'before'
            remain = filter(lambda x: x-current > 0, remain)
            #print str(remain) + 'after'
    return res




def main():
    #m, ions = readdata('rosalind_full.txt')
    m, ions = readdata('test.txt')
    print(m, ions)

    #print m, ions
    #print d
    res = all_seq(ions, d)
    print(res)

main()
