import re

with open("input.txt") as f:
    ans = 0
    for line in f.readlines():
        pattern = "mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, line)
        for match in matches:
            match = match.replace("mul(", "").replace(")", "")
            a, b = match.split(",")
            ans += int(a) * int(b)
    print(ans)
