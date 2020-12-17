import math
import re
from collections import defaultdict
from timeit import timeit


def matches_fields(num, rules):
    fields = []
    for rulekey, ranges in rules.items():
        min1, max1, min2, max2 = ranges
        if min1 <= num <= max1 or min2 <= num <= max2:
            fields.append(rulekey)
    return set(fields)


def parse_input():
    rules = {}
    tickets = []
    rule_str, my_tkt_str, tickets_str = open('day16.txt').read().split('\n\n')
    for line in rule_str.splitlines():
        line = line.strip()
        key, vals = line.split(': ')
        ranges = tuple(int(x) for x in re.match(r'(\d+)-(\d+) or (\d+)-(\d+)', vals).groups())
        rules[key] = ranges

    for tktstr in tickets_str.splitlines():
        if tktstr == 'nearby tickets:': continue
        tktstr = tktstr.strip()
        tkt = tuple([int(x) for x in tktstr.split(',')])
        tickets.append(tkt)

    my_ticket = [int(i) for i in my_tkt_str.split('\n')[1].split(',')]

    return rules, tickets, my_ticket


def part1():
    rules, tickets, my_ticket = parse_input()
    bad = []
    for tkt in tickets:
        for num in tkt:
            if not matches_fields(num, rules):
                bad.append(num)
    print(bad, rules)
    print(sum(bad))


def part2():
    rules, tickets, my_ticket = parse_input()

    fieldnums = defaultdict(lambda: set(rules.keys()))

    for tkt in tickets:
        for fnum, num in enumerate(tkt):
            potential_fields = matches_fields(num, rules)
            if potential_fields:
                fieldnums[fnum] = fieldnums[fnum].intersection(potential_fields)

    field_list = [None] * 20
    seen = set()
    for pos, fields in sorted(list(fieldnums.items()), key=lambda f: len(f[1])):
        fields = fields.difference(seen)
        val = fields.pop()
        seen.add(val)
        field_list[pos] = val

    print(math.prod(myval for myval, field in zip(my_ticket, field_list) if field.startswith('departure ')))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
