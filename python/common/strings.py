
# Toolbox is a set of utility methods to process DNA related sequences

def substrings(string):
    subs = []
    l = len(string)
    for i in range(2, len(string)+1):
        for j in range(l - i + 1):
            ss = string[j:i+j]
            subs.append(ss)
    return subs
