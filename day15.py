from collections import defaultdict
from timeit import timeit



def part1():
    numbers = [9, 6, 0, 10, 18, 2, 1]
    round = 1
    seq = [None]
    while round <= 2020:
        if numbers:
            seq.append(numbers.pop(0))
        else:
            prev = seq[-1]
            if prev in seq[:-1]:
                pos = list(reversed(seq[:-1])).index(prev)
                if pos > -1:
                    seq.append((round-1)-(len(seq[:-1]) - pos - 1))
            else:
                seq.append(0)
        round += 1
    print(seq[-1])


def part2():
    numbers = [9, 6, 0, 10, 18, 2, 1]
    round = 1
    seen = defaultdict(list)
    last_number = None
    while round <= 30000000:
        if numbers:
            last_number = numbers.pop(0)
        elif len(seen[last_number]) == 1:
            last_number = 0
        else:
            last_number = seen[last_number][-1] - seen[last_number][-2]
        seen[last_number].append(round)
        round += 1
    print(last_number)


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
