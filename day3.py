import re
from timeit import timeit


lines = open('day3.txt').readlines()
lines = [list(l.strip()) for l in lines]

def count_trees(dx, dy, x=0, y=0):
    total = 0
    while y < len(lines)-1:
        x = (x + dx) % len(lines[0])
        y += dy
        if lines[y][x] == '#':
            total += 1
    return total


def part1():
    print(count_trees(3, 1))


def part2():
    print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
