import collections

with open("input.txt") as f:
    l, counter = [], collections.Counter()
    for line in f.readlines():
        c1, c2 = line.split()
        l.append(int(c1))
        counter[int(c2)] += 1
    print(sum(a * counter[a] for a in l))
