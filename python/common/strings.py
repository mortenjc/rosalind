
# Toolbox is a set of utility methods to process DNA related sequences

# generate all substrings of a string
def substrings(string):
    subs = []
    l = len(string)
    for i in range(2, len(string)+1):
        for j in range(l - i + 1):
            ss = string[j:i+j]
            subs.append(ss)
    return subs


# check if pattern occurs in a list of strings
def matches(strings, pattern):
    for string in strings:
        #print(f'search for {ss} in {string}')
        if string.find(pattern) == -1:
            return False
    return True
