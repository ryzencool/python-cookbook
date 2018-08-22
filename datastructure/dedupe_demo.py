def dedupe(items):
    seen = set()

    for x in items:
        if x not in seen:
            yield x
            seen.add(x)


l = [1,2,3,3,2,1,2,34,234,32,1]

for x in dedupe(l):
    print(x)

def dedupeDict(items, key= None):
    seen = set()

    for x in items:
        val = x if key is None else key(x)
        if val not in seen:
            yield x
            seen.add(val)


ll = [{'x': 1, 'y': 2}, {'x':1, 'y':3}]

for k in dedupeDict(ll, lambda d: d['x']):
    print(k)