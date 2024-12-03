with open("input.txt") as f:
    list1, list2 = [], []
    for line in f.readlines():
        l1, l2 = line.split()
        list1.append(int(l1))
        list2.append(int(l2))
    print(sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2))))
