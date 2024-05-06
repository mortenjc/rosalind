import toolbox as tb

assert tb.is_start('ATG')
assert not tb.is_start('AUG') # not for RNA
assert not tb.is_start('AAA')

assert tb.is_stop('TAG')
assert tb.is_stop('TGA')
assert tb.is_stop('TAA')

assert tb.aminoseq('ATGAAATAG') == 'MK*'

assert tb.compl('ATCG') == 'TAGC'

assert tb.revcompl('ATCG') == 'CGAT'

assert tb.startcodons('ATGGGGATG') == [0, 6]

assert tb.openframe('ATGGGGTAA') == "MG" # START/M GGG/G STOP
assert tb.openframe('ATGGGG') == "" # START/M GGG/G

assert tb.delintron('ABCDEFGHI', 'DEF') == 'ABCGHI'


r = tb.aminostat('ATCGUGCAT')
assert r['A'] == 2
assert r['T'] == 2
assert r['C'] == 2
assert r['U'] == 1

assert tb.blosum62['AA'] == 4
assert tb.blosum62['PG'] == tb.blosum62['GP']
assert tb.blosum62['YY'] == 7


assert tb.score('!!!') == 0
assert tb.score('III') == 120
