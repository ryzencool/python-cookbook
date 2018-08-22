from operator import attrgetter

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
            return 'user({})'.format(self.name)


l = [User(2), User(1), User(3)]

b = sorted(l, key = lambda b: b.name)
print(b)

