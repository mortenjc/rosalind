import toolbox as tb


assert tb.is_start('AUG')
assert tb.is_start('ATG')
assert not tb.is_start('AAA')

assert tb.is_stop('TAG')
assert tb.is_stop('TGA')
assert tb.is_stop('TAA')

assert tb.revseq('ABCD') == 'DCBA'

assert tb.aminoseq('ATGAAATAG') == 'MK*'

assert tb.compl('ATCG') == 'TAGC'

assert tb.revcompl('ATCG') == 'CGAT'

assert tb.startpositions('ATGGGGATG') == [0, 6]
