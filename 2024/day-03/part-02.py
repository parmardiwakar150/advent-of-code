import re
import bisect

with open("input.txt") as f:
    ans = 0
    line = f.read()
    valid = []
    invalid = []
    valid_pattern = "do\(\)"
    invalid_pattern = "don't\(\)"
    for match in re.finditer(valid_pattern, line):
        valid.append(match.start())
    for match in re.finditer(invalid_pattern, line):
        invalid.append(match.start())
    pattern = "mul\(\d{1,3},\d{1,3}\)"
    matches = re.finditer(pattern, line)
    for match in matches:
        i = bisect.bisect_left(invalid, match.start())
        if i > 0:
            j = bisect.bisect_left(valid, match.start())
            if j == 0 or valid[j - 1] < invalid[i - 1]:
                continue
        c, d = match.group().replace("mul(", "").replace(")", "").split(",")
        ans += int(c) * int(d)
    print(ans)
