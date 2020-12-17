import time
from collections import Counter
from operator import itemgetter
from timeit import timeit
f = open('day13.txt')
start_stamp = int(f.readline().strip())
schedule = [int(s) if s != 'x' else 'x' for s in f.readline().strip().split(',')]


def part1():
    t = 0
    times = Counter()
    for bid in [int(x) for x in schedule if x != 'x']:
        times[bid] = 0
        while times[bid] < start_stamp:
            times[bid] += bid
    busid, deptime = times.most_common()[-1]
    wait = deptime - start_stamp
    print(wait * busid)


def part_two(data):
    buses = [x for x in data if type(x) is int]
    mods = [0 if i == 0 else v - (i % v) for i, v in enumerate(data) if v != 'x']

    t, step = 0, 1
    for bid, mod in zip(buses, mods):
        while t % bid != mod:
            t += step
        step *= bid
    return t


def part2():

    print(part_two(schedule))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
