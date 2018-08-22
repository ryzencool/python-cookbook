from collections import OrderedDict

def ordered_dict():
    d = OrderedDict()
    d['java'] = 1
    d['python'] = 2
    d['php'] = 4

    print({k:d[k] for k in d})

ordered_dict()