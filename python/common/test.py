import toolbox as tb
import strings as s
import intlists as il

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

assert s.reverse('ABCD') == 'DCBA'
assert s.reverse('NETROM') == 'MORTEN'

assert s.substrings('') == []
assert s.substrings('AB') == ['AB']
assert s.substrings('ABC') == ['AB', 'ABC', 'BC']
assert s.substrings('AAAA') == ['AA', 'AAA', 'AAAA']

assert s.findall('AAABBAAAABAAA', 'AAA') == [1,6,7,11]

assert s.contiguous_matches('ABCDEF', 0, 'DEFXXX') == 0
assert s.contiguous_matches('ABCDEF', 1, 'DEFXXX') == 0
assert s.contiguous_matches('ABCDEF', 2, 'DEFXXX') == 0
assert s.contiguous_matches('ABCDEF', 3, 'DEFXXX') == 3
assert s.contiguous_matches('ABCDEF', 4, 'EFXXXX') == 2
assert s.contiguous_matches('ABCDEF', 5, 'FXXXXX') == 1
assert s.contiguous_matches('ABCDEF', 4, 'XXXXXX') == 0
assert s.contiguous_matches('ABCDEF', 6, 'XXXXXXX') == 0

assert s.longest_overlap('ABCDEF', 'DEFXYZ') == (3,3)
assert s.longest_overlap('ABCDEF', 'ABCDEF') == (0,6)
assert s.longest_overlap('ABCDEF', 'ABCDEFG') == (0,6)
assert s.longest_overlap('ABCDEF', 'ABCDE') == (0,5)
assert s.longest_overlap('ABCDEF', 'GHIJKL') == (0,0)

assert len(il.long_sseq([1])) == 1
assert len(il.long_sseq([1,2])) == 2
assert len(il.long_sseq(range(700))) == 700
assert len(il.long_sseq(range(700)[::-1])) == 1
assert len(il.long_sseq([8,3,4,6,5,2,0,7,9,1])) == 5
assert il.long_sseq([8,3,4,6,5,2,0,7,9,1]) == [3,4,6,7,9]
assert il.long_sseq(range(700)) == list(range(700))
assert il.long_sseq([10, 20, 2, 5, 3, 8, 8, 25, 6]) == [2, 5, 8, 25]
