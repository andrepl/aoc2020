import re
from timeit import timeit

LINES = [l.strip() for l in open('day19.txt').readlines()]


ops = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b
}

def solve(eq):
    tokens = eq.split(' ')
    first = int(tokens.pop(0))
    while tokens:
        op = ops[tokens.pop(0)]
        nxt = int(tokens.pop(0))
        first = op(first, nxt)
    return first


def add_sub(m):
    a, b = m.groups()
    return str(int(a) + int(b))


def mul_sub(m):
    a, b = m.groups()
    return str(int(a) * int(b))


def solve2(eq):
    while '+' in eq or '*' in eq:
        while re.search(r'(\d+) \+ (\d+)', eq):
            eq = re.sub(r'(\d+) \+ (\d+)', add_sub, eq)
        while re.search(r'(\d+) \* (\d+)', eq):
            eq = re.sub(r'(\d+) \* (\d+)', mul_sub, eq)
    return int(eq)


def solve_str(m):
    return str(solve(m.groups()[0]))


def solve_str2(m):
    return str(solve2(m.groups()[0]))


def simplify(eq):
    while '(' in eq:
        eq = re.sub(r'\(([^)(]+)\)', solve_str, eq)
    return solve(eq)


def simplify2(eq):
    while '(' in eq:
        eq = re.sub(r'\(([^)(]+)\)', solve_str2, eq)
    return solve2(eq)


def part1():
    pass
    print(sum(simplify(line) for line in LINES))


def part2():
    # print(simplify2('2 * 3 + (4 * 5)'))
    print(sum(simplify2(line) for line in LINES))


if __name__ == '__main__':
    print("Part 1: ", end="")
    # print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
