from collections import defaultdict

d = defaultdict(list)
d['a'].append("1")
d['a'].append("2")
print(d['a'])

d = defaultdict(set)

d['b'].add("1")
d['b'].add("1")
d['b'].add("1")

print(d['b'])