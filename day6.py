import sys
from timeit import timeit


records = [r.split('\n') for r in open('day6.txt').read().split('\n\n')]


def part1():
    print(sum(len(set.union(*(set(r) for r in rec))) for rec in records))
        

def part2():
    print(sum(len(set.intersection(*(set(r) for r in rec))) for rec in records))



if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
