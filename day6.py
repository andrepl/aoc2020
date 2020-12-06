import sys
from timeit import timeit


records = [r.split('\n') for r in open('day6.txt').read().split('\n\n')]

def part1():
    tot = 0
    for rec in records:
        recset = set()
        for person in rec:
            recset.update(person)
        tot += len(recset)
    print(tot)
        

def part2():
    tot = 0
    for rec in records:
        recset = set.intersection(*(set(r) for r in rec))
        tot += len(recset)
    print(tot)


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
