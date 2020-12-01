from timeit import timeit
import itertools
import math


nums = [int(x) for x in open('day1.txt').readlines()]


def sums2020(numbers, n):
    for items in itertools.combinations(numbers, n):
        if sum(items) == 2020:
            return math.prod(items)


def part1():
    print(sums2020(nums, 2))


def part2():
    print(sums2020(nums, 3))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
