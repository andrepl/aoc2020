from collections import defaultdict
from timeit import timeit
import re


MAP = defaultdict(list)
for line in open('day7.txt').readlines():
    container, contents = line.strip('.').split(' bags contain ')
    for c in contents.split(', '):
        if c == 'no other bags':
            continue
        m = re.match(r'(\d+)\s(\w+\s\w+)\sbags?', c)
        MAP[container].append((m.groups()[1], int(m.groups()[0])))


def part1():
    def chk(b):
        for k, contents in MAP.items():
            if b in (c[0] for c in contents):
                yield k
    q = [('shiny gold', 1)]
    visited = set()
    while q:
        k, v = q.pop(0)
        for r in chk(k):
            if r not in visited:
                visited.add(r)
                q.append((r, v + 1))
    print(len(visited))


def part2():

    def get_cost(bag):
        return 1 + sum(get_cost(a) * b for a, b in MAP[bag])

    print(get_cost('shiny gold') - 1)

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
