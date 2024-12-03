def is_safe(levels):
    diffs = []
    n = len(levels)
    for i in range(n - 1):
        diffs.append(int(levels[i + 1]) - int(levels[i]))
    return all(1 <= val <= 3 for val in diffs) or all(-3 <= val <= -1 for val in diffs)


with open("input.txt") as f:
    count = 0
    for line in f.readlines():
        line = line.split()
        n = len(line)
        if is_safe(line):
            count += 1
            continue
        for i in range(n):
            if is_safe(line[:i] + line[i + 1 :]):
                count += 1
                break
    print(count)
