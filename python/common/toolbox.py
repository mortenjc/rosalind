# Toolbox is a set of utility methods to process DNA related sequences
import strings
import numpy as np

#
## Lookup tables
#

# DNA codons -> Amino acids
codontab = {
    'TCA': 'S',
    'TCC': 'S',
    'TCG': 'S',
    'TCT': 'S',
    'TTC': 'F',
    'TTT': 'F',
    'TTA': 'L',
    'TTG': 'L',
    'TAC': 'Y',
    'TAT': 'Y',
    'TAA': '*',
    'TAG': '*',
    'TGC': 'C',
    'TGT': 'C',
    'TGA': '*',
    'TGG': 'W',
    'CTA': 'L',
    'CTC': 'L',
    'CTG': 'L',
    'CTT': 'L',
    'CCA': 'P',
    'CCC': 'P',
    'CCG': 'P',
    'CCT': 'P',
    'CAC': 'H',
    'CAT': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'CGT': 'R',
    'ATA': 'I',
    'ATC': 'I',
    'ATT': 'I',
    'ATG': 'M',
    'ACA': 'T',
    'ACC': 'T',
    'ACG': 'T',
    'ACT': 'T',
    'AAC': 'N',
    'AAT': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGC': 'S',
    'AGT': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GTA': 'V',
    'GTC': 'V',
    'GTG': 'V',
    'GTT': 'V',
    'GCA': 'A',
    'GCC': 'A',
    'GCG': 'A',
    'GCT': 'A',
    'GAC': 'D',
    'GAT': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGA': 'G',
    'GGC': 'G',
    'GGG': 'G',
    'GGT': 'G',
}

# BLOSUM62 Scoring matrix for protein string alignment
# Converted to dictionary from https://rosalind.info/glossary/blosum62/
blosum62 = {
    'AA': 4,
    'AC': 0,
    'CA': 0,
    'AD': -2,
    'DA': -2,
    'AE': -1,
    'EA': -1,
    'AF': -2,
    'FA': -2,
    'AG': 0,
    'GA': 0,
    'AH': -2,
    'HA': -2,
    'AI': -1,
    'IA': -1,
    'AK': -1,
    'KA': -1,
    'AL': -1,
    'LA': -1,
    'AM': -1,
    'MA': -1,
    'AN': -2,
    'NA': -2,
    'AP': -1,
    'PA': -1,
    'AQ': -1,
    'QA': -1,
    'AR': -1,
    'RA': -1,
    'AS': 1,
    'SA': 1,
    'AT': 0,
    'TA': 0,
    'AV': 0,
    'VA': 0,
    'AW': -3,
    'WA': -3,
    'AY': -2,
    'YA': -2,
    'CC': 9,
    'CD': -3,
    'DC': -3,
    'CE': -4,
    'EC': -4,
    'CF': -2,
    'FC': -2,
    'CG': -3,
    'GC': -3,
    'CH': -3,
    'HC': -3,
    'CI': -1,
    'IC': -1,
    'CK': -3,
    'KC': -3,
    'CL': -1,
    'LC': -1,
    'CM': -1,
    'MC': -1,
    'CN': -3,
    'NC': -3,
    'CP': -3,
    'PC': -3,
    'CQ': -3,
    'QC': -3,
    'CR': -3,
    'RC': -3,
    'CS': -1,
    'SC': -1,
    'CT': -1,
    'TC': -1,
    'CV': -1,
    'VC': -1,
    'CW': -2,
    'WC': -2,
    'CY': -2,
    'YC': -2,
    'DD': 6,
    'DE': 2,
    'ED': 2,
    'DF': -3,
    'FD': -3,
    'DG': -1,
    'GD': -1,
    'DH': -1,
    'HD': -1,
    'DI': -3,
    'ID': -3,
    'DK': -1,
    'KD': -1,
    'DL': -4,
    'LD': -4,
    'DM': -3,
    'MD': -3,
    'DN': 1,
    'ND': 1,
    'DP': -1,
    'PD': -1,
    'DQ': 0,
    'QD': 0,
    'DR': -2,
    'RD': -2,
    'DS': 0,
    'SD': 0,
    'DT': -1,
    'TD': -1,
    'DV': -3,
    'VD': -3,
    'DW': -4,
    'WD': -4,
    'DY': -3,
    'YD': -3,
    'EE': 5,
    'EF': -3,
    'FE': -3,
    'EG': -2,
    'GE': -2,
    'EH': 0,
    'HE': 0,
    'EI': -3,
    'IE': -3,
    'EK': 1,
    'KE': 1,
    'EL': -3,
    'LE': -3,
    'EM': -2,
    'ME': -2,
    'EN': 0,
    'NE': 0,
    'EP': -1,
    'PE': -1,
    'EQ': 2,
    'QE': 2,
    'ER': 0,
    'RE': 0,
    'ES': 0,
    'SE': 0,
    'ET': -1,
    'TE': -1,
    'EV': -2,
    'VE': -2,
    'EW': -3,
    'WE': -3,
    'EY': -2,
    'YE': -2,
    'FF': 6,
    'FG': -3,
    'GF': -3,
    'FH': -1,
    'HF': -1,
    'FI': 0,
    'IF': 0,
    'FK': -3,
    'KF': -3,
    'FL': 0,
    'LF': 0,
    'FM': 0,
    'MF': 0,
    'FN': -3,
    'NF': -3,
    'FP': -4,
    'PF': -4,
    'FQ': -3,
    'QF': -3,
    'FR': -3,
    'RF': -3,
    'FS': -2,
    'SF': -2,
    'FT': -2,
    'TF': -2,
    'FV': -1,
    'VF': -1,
    'FW': 1,
    'WF': 1,
    'FY': 3,
    'YF': 3,
    'GG': 6,
    'GH': -2,
    'HG': -2,
    'GI': -4,
    'IG': -4,
    'GK': -2,
    'KG': -2,
    'GL': -4,
    'LG': -4,
    'GM': -3,
    'MG': -3,
    'GN': 0,
    'NG': 0,
    'GP': -2,
    'PG': -2,
    'GQ': -2,
    'QG': -2,
    'GR': -2,
    'RG': -2,
    'GS': 0,
    'SG': 0,
    'GT': -2,
    'TG': -2,
    'GV': -3,
    'VG': -3,
    'GW': -2,
    'WG': -2,
    'GY': -3,
    'YG': -3,
    'HH': 8,
    'HI': -3,
    'IH': -3,
    'HK': -1,
    'KH': -1,
    'HL': -3,
    'LH': -3,
    'HM': -2,
    'MH': -2,
    'HN': 1,
    'NH': 1,
    'HP': -2,
    'PH': -2,
    'HQ': 0,
    'QH': 0,
    'HR': 0,
    'RH': 0,
    'HS': -1,
    'SH': -1,
    'HT': -2,
    'TH': -2,
    'HV': -3,
    'VH': -3,
    'HW': -2,
    'WH': -2,
    'HY': 2,
    'YH': 2,
    'II': 4,
    'IK': -3,
    'KI': -3,
    'IL': 2,
    'LI': 2,
    'IM': 1,
    'MI': 1,
    'IN': -3,
    'NI': -3,
    'IP': -3,
    'PI': -3,
    'IQ': -3,
    'QI': -3,
    'IR': -3,
    'RI': -3,
    'IS': -2,
    'SI': -2,
    'IT': -1,
    'TI': -1,
    'IV': 3,
    'VI': 3,
    'IW': -3,
    'WI': -3,
    'IY': -1,
    'YI': -1,
    'KK': 5,
    'KL': -2,
    'LK': -2,
    'KM': -1,
    'MK': -1,
    'KN': 0,
    'NK': 0,
    'KP': -1,
    'PK': -1,
    'KQ': 1,
    'QK': 1,
    'KR': 2,
    'RK': 2,
    'KS': 0,
    'SK': 0,
    'KT': -1,
    'TK': -1,
    'KV': -2,
    'VK': -2,
    'KW': -3,
    'WK': -3,
    'KY': -2,
    'YK': -2,
    'LL': 4,
    'LM': 2,
    'ML': 2,
    'LN': -3,
    'NL': -3,
    'LP': -3,
    'PL': -3,
    'LQ': -2,
    'QL': -2,
    'LR': -2,
    'RL': -2,
    'LS': -2,
    'SL': -2,
    'LT': -1,
    'TL': -1,
    'LV': 1,
    'VL': 1,
    'LW': -2,
    'WL': -2,
    'LY': -1,
    'YL': -1,
    'MM': 5,
    'MN': -2,
    'NM': -2,
    'MP': -2,
    'PM': -2,
    'MQ': 0,
    'QM': 0,
    'MR': -1,
    'RM': -1,
    'MS': -1,
    'SM': -1,
    'MT': -1,
    'TM': -1,
    'MV': 1,
    'VM': 1,
    'MW': -1,
    'WM': -1,
    'MY': -1,
    'YM': -1,
    'NN': 6,
    'NP': -2,
    'PN': -2,
    'NQ': 0,
    'QN': 0,
    'NR': 0,
    'RN': 0,
    'NS': 1,
    'SN': 1,
    'NT': 0,
    'TN': 0,
    'NV': -3,
    'VN': -3,
    'NW': -4,
    'WN': -4,
    'NY': -2,
    'YN': -2,
    'PP': 7,
    'PQ': -1,
    'QP': -1,
    'PR': -2,
    'RP': -2,
    'PS': -1,
    'SP': -1,
    'PT': -1,
    'TP': -1,
    'PV': -2,
    'VP': -2,
    'PW': -4,
    'WP': -4,
    'PY': -3,
    'YP': -3,
    'QQ': 5,
    'QR': 1,
    'RQ': 1,
    'QS': 0,
    'SQ': 0,
    'QT': -1,
    'TQ': -1,
    'QV': -2,
    'VQ': -2,
    'QW': -2,
    'WQ': -2,
    'QY': -1,
    'YQ': -1,
    'RR': 5,
    'RS': -1,
    'SR': -1,
    'RT': -1,
    'TR': -1,
    'RV': -3,
    'VR': -3,
    'RW': -3,
    'WR': -3,
    'RY': -2,
    'YR': -2,
    'SS': 4,
    'ST': 1,
    'TS': 1,
    'SV': -2,
    'VS': -2,
    'SW': -3,
    'WS': -3,
    'SY': -2,
    'YS': -2,
    'TT': 5,
    'TV': 0,
    'VT': 0,
    'TW': -2,
    'WT': -2,
    'TY': -2,
    'YT': -2,
    'VV': 4,
    'VW': -3,
    'WV': -3,
    'VY': -1,
    'YV': -1,
    'WW': 11,
    'WY': 2,
    'YW': 2,
    'YY': 7,
}

# DNA complementation
compltab = {"A": "T", "T": "A", "G": "C", "C": "G"}

# calculated from multiplicity
codonmult = {
    'S': 6,
    'F': 2,
    'L': 6,
    'Y': 2,
    '*': 3,
    'C': 2,
    'W': 1,
    'P': 4,
    'H': 2,
    'Q': 2,
    'R': 6,
    'I': 3,
    'M': 1,
    'T': 4,
    'N': 2,
    'K': 2,
    'V': 4,
    'A': 4,
    'D': 2,
    'E': 2,
    'G': 4,
}


#
## Simple 'string' functions
#


def qscore(qstr):
    res = 0
    for ch in qstr:
        assert ch >= '!' and ch <= 'Z', ch
        res += ord(ch) - ord('!')
    return res


def aminostat(seq):
    s = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'U': 0}
    for i in seq:
        s[i] += 1
    return s


# Return the amino acid for a DNA nucleotide sequence
def amino(nuclseq):
    assert len(nuclseq) == 3
    return codontab[nuclseq]


# Return the complement to a DNA sequence
def compl(nuclseq):
    s = ''
    for i in range(len(nuclseq)):
        s += compltab[nuclseq[i]]
    return s


# Return the reversed complement to a DNA sequence
def revcompl(nuclseq):
    s = ''
    for i in range(len(nuclseq)):
        s += compltab[nuclseq[i]]
    return strings.reverse(s)


#
## Codon functions
#


def multiplicity():
    s = set()
    d = {}
    for t in codontab:
        amino = codontab[t]
        if amino in s:
            d[amino] += 1
        else:
            s.add(amino)
            d[amino] = 1
    print(d)


# Is this a DNA START codon?
def is_start(seq):
    return seq == 'ATG'


# Is this s DNA STOP codon?
def is_stop(seq):
    return codontab[seq] == '*'


# Return a list, possibly empty, of indexes for START codons
def startcodons(nuclseq):
    pos = []
    for i in range(0, len(nuclseq), 3):
        cod = nuclseq[i : i + 3]
        if is_start(cod):
            pos.append(i)
    return pos


# Given a DNA nucleotide sequence string, return the amino acid sequence
def aminoseq(nuclseq):
    s = ''
    for i in range(0, len(nuclseq), 3):
        s += amino(nuclseq[i : i + 3])
    return s


#
## Slightly advanced
#


# Actually delete a substring, no checking for DNA/RNA validity
def delintron(string, intron):
    i = string.find(intron)
    if i == -1:
        return string
    s1 = string[:i]
    s2 = string[i + len(intron) :]
    return s1 + s2


# Given a DNA nucleotide sequence string, return the amino acid sequence
# between the first START codon (included) and the first STOP codon (excluded)
def openframe(nuclseq):
    state = 0  # 0 initial, 1 started, 2 stopped
    s = ''
    for i in range(0, len(nuclseq), 3):
        codon = nuclseq[i : i + 3]
        if len(codon) != 3:
            break
        if state == 0:
            if is_start(codon):
                state = 1
                s = amino(codon)
                continue
        elif state == 1:
            if is_stop(codon):
                return s
            else:
                s += amino(codon)
    return ''


def global_alignment(s1, s2, parms):
    match, mismatch, gap = parms
    print('costs', match, mismatch, gap)

    def mineditlen(s, t):
        gp = gap  # gap penalty
        m = len(s)
        n = len(t)
        C = np.ndarray((m + 1, n + 1))
        for i in range(m + 1):
            C[i, 0] = i * gp
        for j in range(n + 1):
            C[0, j] = j * gp

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if C[i - 1, j - 1] == C[i, j]:
                    substcost = match
                else:
                    substcost = mismatch
                minval = min(
                    C[i - 1, j] + gp, C[i, j - 1] + gp, C[i - 1, j - 1] + substcost
                )
                # print(f'({i},{j}) {s[i-1]}, {t[j-1]}: {substcost} (min {minval})')
                C[i, j] = minval

        print(C)
        print('     ', '  '.join(s2))
        for i in range(len(s1) + 1):
            if i == 0:
                print(' ', C[i])
            else:
                print(s1[i - 1], C[i])
        return C, C[m, n]

    def backtrack(C, s, t):
        i = len(s)
        j = len(t)
        s2 = ''
        t2 = ''
        matches = 0
        while i != 0 or j != 0:
            minval = min(C[i - 1, j - 1], C[i - 1, j], C[i, j - 1])
            if minval == C[i - 1, j - 1]:  # subst or match
                if s[i - 1] == t[j - 1]:
                    matches += 1
                s2 = s[i - 1] + s2
                t2 = t[j - 1] + t2
                i -= 1
                j -= 1
            elif minval == C[i - 1, j]:  # ins?
                s2 = s[i - 1] + s2
                t2 = '-' + t2
                i -= 1
            else:
                s2 = '-' + s2
                t2 = t[j - 1] + t2
                j -= 1

        return s2, t2, matches

    M, score = mineditlen(s1, s2)
    a, b, matches = backtrack(M, s1, s2)
    print(a)
    print(b)
