import itertools
from timeit import timeit

numbers = [int(l.strip()) for l in open('day9.txt').readlines()]


def solve(preamble_length):
    for i, n in enumerate(numbers):
        if i >= preamble_length:
            pairs = [pair for pair in itertools.combinations(numbers[i-preamble_length:i], 2) if sum(pair) == n]
            if not pairs:
                print('pairs for {}'.format(n), pairs)
                return


def part1():
    solve(25)


def part2():
    size = 2
    target = 23278925
    while size < len(numbers):
        for i in range(len(numbers)-size):
            if sum(numbers[i:i+size]) == target:
                print(max(numbers[i:i+size]) + min(numbers[i:i+size]))
                return
        size += 1
        print('size {}'.format(size))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
