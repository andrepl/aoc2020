import itertools
import math
import time

nums = [int(x) for x in open('day1.txt').readlines()]


def sums2020(numbers, n):
    for items in itertools.combinations(numbers, n):
        if sum(items) == 2020:
            return math.prod(items)


def part1():
    return sums2020(nums, 2)


def part2():
    return sums2020(nums, 3)


if __name__ == '__main__':
    start = time.time()
    print(part1())
    end = time.time()
    print("part1 in {}s". format(end-start))
    start = time.time()
    print(part2())
    end = time.time()
    print("part2 in {}s". format(end-start))