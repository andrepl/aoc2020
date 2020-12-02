import re
from timeit import timeit


# lines = open('day2.txt').readlines()
lines = [re.match(r'(\d+)-(\d+)\s([a-z]): (\w+)', x).groups() for x in open('day2.txt').readlines()]
print(lines)


def part1():
    valid = 0
    for minc, maxc, letter, pw in lines:
        if int(minc) <= pw.count(letter) <= int(maxc):
            valid += 1
    print(valid)


def part2():
    valid = 0
    for p1, p2, letter, pw in lines:
        a = pw[int(p1)-1] == letter
        b = pw[int(p2)-1] == letter
        if (a and not b) or (b and not a):
            valid += 1
    print(valid)


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
