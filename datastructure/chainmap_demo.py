from collections import ChainMap


a = {
    'a': 1,
    'b': 2, 
    'c': 3
}

b = {
    'd': 4,
    'e': 5,
    'f': 6
}

d = ChainMap(a,b)

for k in d:
    print(k, d[k])