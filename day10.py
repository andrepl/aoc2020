
from math import factorial, floor
from itertools import groupby

# Import data
data = sorted([0] + [int(i) for i in open('day10.txt').readlines()])
data.append(max(data) + 3)

MAX = 3

# Create a list of differences (i.e. [0, 3, 4, 5, 8] -> [3, 1, 1, 3])
diffs = [data[i] - data[i-1] for i in range(1, len(data))]

def arrange(n):
    """Given some number of consecutive integers (n), return the number of valid configurations."""
    total = 1
    for diff in range(2, MAX + 1):
        for groups in range(1, floor(n / diff) + 1):
            length = n - groups * (diff - 1)
            total += factorial(length) / (factorial(length - groups) * factorial(groups))

    return total

total = 1
for i, (value, l) in enumerate((groups := groupby(diffs))):
    if value == 1:
        total *= arrange(sum(1 for i in l))
    elif value == 2:
        if i > 0 and groups[i - 1][0] == 1:
            total *= 2
        if groups[i + 1][0] == 1:
            total *= 2

print(int(total))
