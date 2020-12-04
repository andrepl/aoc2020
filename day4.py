import re
from timeit import timeit

lines = open('day4.txt').readlines()
lines = [l.strip() for l in lines]

cards = []
pplines = []
for line in lines:
    if line == '':
        cards.append(pplines)
        pplines = []
    else:
        pplines.append(line)
cards.append(pplines)

print(cards)

def parse_card(pplines):
    pp = dict()
    for line in pplines:
        tups = line.split(' ')
        for tup in tups:
            k, v = tup.split(':', 1)
            pp[k] = v
    return pp

def valhgt(v):
    match = re.match(r'(\d+)(in|cm)', v)
    if match is None:
        return False
    qty, unit = match.groups()
    qty = int(qty)
    if unit == 'cm':
        if qty < 150:
            return False
        if qty > 193:
            return False
    elif unit == 'in':
        if qty < 59:
            return False
        if qty > 76:
            return False
    else:
        return False
    return True

REQ = 'byr iyr eyr hgt hcl ecl pid'.split(' ')
REQ2 = dict(byr=lambda v: 1920 <= int(v) <= 2002,
            iyr=lambda v: 2010 <= int(v) <= 2020,
            eyr=lambda v: 2020 <= int(v) <= 2030,
            hgt=valhgt,
            hcl=lambda v: re.match(r'#[0-9a-f]{6}', v) is not None,
            ecl=lambda v: v in 'amb blu brn gry grn hzl oth'.split(' '),
            pid=lambda v: len(v) == 9 and re.match(r'^\d+$', v)
            )


def isvalid(c):
    for k in REQ:
        if k not in c:
            return False
    return True

def isvalid2(c):
    if not isvalid(c):
        return False

    for k, validator in REQ2.items():
        if not validator(c[k]):
            return False
    return True

def part1():
    valid = 0
    for card in cards:
        card = parse_card(card)
        if isvalid(card):
            valid += 1
    print(valid)


def part2():
    valid = 0
    for card in cards:
        card = parse_card(card)
        if isvalid2(card):
            valid += 1
    print(valid)


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
