import re
from timeit import timeit

cardstrs = [re.split('\s+', c) for c in open('day4.txt').read().split('\n\n')]
cards = [dict(c.split(':') for c in cs) for cs in cardstrs]


def validate_height(v):
    match = re.match(r'(\d+)(in|cm)', v)
    if match is None:
        return False
    qty, unit = match.groups()
    qty = int(qty)
    if unit == 'cm':
        return 150 <= qty <= 193
    elif unit == 'in':
        return 59 <= qty <= 76
    return False


REQ = dict(
    byr=lambda v: 1920 <= int(v) <= 2002,
    iyr=lambda v: 2010 <= int(v) <= 2020,
    eyr=lambda v: 2020 <= int(v) <= 2030,
    hgt=validate_height,
    hcl=lambda v: re.match(r'^#[0-9a-f]{6}$', v) is not None,
    ecl=lambda v: v in 'amb blu brn gry grn hzl oth'.split(' '),
    pid=lambda v: re.match(r'^\d{9}$', v) is not None
)


def isvalid(c):
    for k in REQ:
        if k not in c:
            return False
    return True


def isvalid2(c):
    if not isvalid(c):
        return False

    for k, validator in REQ.items():
        if not validator(c[k]):
            return False
    return True


def part1():
    print(len([c for c in cards if isvalid(c)]))


def part2():
    print(len([c for c in cards if isvalid2(c)]))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
