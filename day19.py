import regex
import time
from timeit import timeit


RULES, INPUTS = open('day19.txt').read().split('\n\n')
RULES = [r.strip() for r in RULES.splitlines()]
INPUTS = [r.strip() for r in INPUTS.splitlines()]


def parse_rule(s):
    if '|' in s:
        return tuple([parse_rule(i) for i in s.split(' | ')])
    elif s.startswith('"'):
        return s[1:-1]
    else:
        return [int(i) for i in s.split(' ')]


def tree_to_regex(t):
    s = ''
    if isinstance(t, str):
        s += t
    elif isinstance(t, list):
        s += "".join([tree_to_regex(tnode) for tnode in t])
    elif isinstance(t, tuple):
        s += "(?:{}|{})".format(*[tree_to_regex(tnode) for tnode in t])
    return s


def build_tree(rule, rules):
    if isinstance(rule, tuple):
        return [(build_tree(rule[0], rules), build_tree(rule[1], rules))]
    elif isinstance(rule, list):
        return [build_tree(rules[int(r)], rules) for r in rule]
    else:
        return [rule]


def part1():
    rules = {}
    for line in RULES:
        k, v = line.split(': ')
        rules[int(k)] = parse_rule(v)
    print(rules)
    tree = build_tree(rules[0], rules)
    print(tree)

    pat = tree_to_regex(tree)
    pat += ')$'
    pat = '^(' + pat
    ctr = 0
    for inp in INPUTS:
        if regex.match(pat, inp):
            ctr += 1
    print(ctr)


def part2():
    rules = {}
    for line in RULES:
        k, v = line.split(': ')
        rules[int(k)] = parse_rule(v)

    for k, v in rules.items():
        print("{}: {}".format(k, v))
    pat = '^(' + tree_to_regex(build_tree(rules[8], rules)) + ')+'
    pat += '(' + tree_to_regex(build_tree(rules[11], rules)) + '|' + tree_to_regex(build_tree(rules[42], rules)) + '(?2)' + tree_to_regex(build_tree(rules[31], rules)) + ')$'
    print(pat)
    ctr = 0
    for inp in INPUTS:
        if regex.match(pat, inp):
            ctr += 1
    print(ctr)


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
