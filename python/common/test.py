import toolbox as tb
import strings as s

assert tb.is_start('ATG')
assert not tb.is_start('AUG') # not for RNA
assert not tb.is_start('AAA')

assert tb.is_stop('TAG')
assert tb.is_stop('TGA')
assert tb.is_stop('TAA')

assert tb.revseq('ABCD') == 'DCBA'

assert tb.aminoseq('ATGAAATAG') == 'MK*'

assert tb.compl('ATCG') == 'TAGC'

assert tb.revcompl('ATCG') == 'CGAT'

assert tb.startcodons('ATGGGGATG') == [0, 6]

assert tb.openframe('ATGGGGTAA') == "MG" # START/M GGG/G STOP
assert tb.openframe('ATGGGG') == "" # START/M GGG/G

assert tb.delintron('ABCDEFGHI', 'DEF') == 'ABCGHI'

assert s.substrings('') == []
assert s.substrings('AB') == ['AB']
print(s.substrings('ABC'))
assert s.substrings('ABC') == ['AB', 'ABC', 'BC']
assert s.substrings('AAAA') == ['AA', 'AAA', 'AAAA']

assert s.findall('AAABBAAAABAAA', 'AAA') == [1,6,7,11]
