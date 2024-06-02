import sys

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, strings = f.readfasta(lines)
# print(n, names, strings)

assert n == 1

orgstr = strings[0]
revc = tb.revcompl(orgstr)
ss = s.substrings(orgstr)
ss2 = [i for i in ss if len(i) > 3 and len(i) < 13 and len(i) % 2 == 0]
# print(orgstr)
# print(tb.revseq(orgstr))
# print(revc)
# print(ss2)
# sys.exit()


res = {}
for sstr in ss2:
    # print('testing', sstr)
    l = len(sstr)
    idxs = s.findall(orgstr, sstr)
    assert idxs != []
    # print(idxs)
    for idx in idxs:
        # print(orgstr[idx-1:idx-1+l])
        assert orgstr[idx - 1 : idx - 1 + l] == sstr
        if sstr == tb.revcompl(sstr):
            # print(idx, len(sstr))
            res[idx] = len(sstr)

for i in sorted(res.items()):
    print(f'{i[0]}\t{i[1]}')
print()
