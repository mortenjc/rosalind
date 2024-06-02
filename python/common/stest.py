import strings as s

assert s.reverse('ABCD') == 'DCBA'
assert s.reverse('NETROM') == 'MORTEN'

assert s.substrings('') == []
assert s.substrings('AB') == ['AB']
assert s.substrings('ABC') == ['AB', 'ABC', 'BC']
assert s.substrings('AAAA') == ['AA', 'AAA', 'AAAA']

assert s.findall('AAABBAAAABAAA', 'AAA') == [1, 6, 7, 11]

assert s.contiguous_matches('ABCDEF', 0, 'DEFXXX') == 0
assert s.contiguous_matches('ABCDEF', 1, 'DEFXXX') == 0
assert s.contiguous_matches('ABCDEF', 2, 'DEFXXX') == 0
assert s.contiguous_matches('ABCDEF', 3, 'DEFXXX') == 3
assert s.contiguous_matches('ABCDEF', 4, 'EFXXXX') == 2
assert s.contiguous_matches('ABCDEF', 5, 'FXXXXX') == 1
assert s.contiguous_matches('ABCDEF', 4, 'XXXXXX') == 0
assert s.contiguous_matches('ABCDEF', 6, 'XXXXXXX') == 0

assert s.longest_overlap('ABCDEF', 'DEFXYZ') == (3, 3)
assert s.longest_overlap('ABCDEF', 'ABCDEF') == (0, 6)
assert s.longest_overlap('ABCDEF', 'ABCDEFG') == (0, 6)
assert s.longest_overlap('ABCDEF', 'ABCDE') == (0, 5)
assert s.longest_overlap('ABCDEF', 'GHIJKL') == (0, 0)
