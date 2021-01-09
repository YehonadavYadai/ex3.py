import copy

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

if __name__ == '__main__':
    l = {1:'a', 2:'c'}
    b = l.keys()
    d = list()
    for i in b:
        d.append(i)
    l[3] = 'v'
    print(d)
