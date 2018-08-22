a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "x": 1,
    "k": 2,
    "j": 3
}

print(a.keys() & b.keys())

print(a.keys() - b.keys())

print({x: a[x] for x in a.keys() - {"x"}})