import sys
from timeit import timeit


lines = open('day5.txt').readlines()
lines = [l.strip() for l in lines]

seat_ids = set()

def part1():
    for line in lines:
        row, col = line[:7], line[-3:]
        row = int(row.replace('F', '0').replace('B', '1'), 2)
        col = int(col.replace('L', '0').replace('R', '1'), 2)
        seat_ids.add((row * 8) + col)
    print(max(seat_ids))


def part2():
    for sid in range(min(seat_ids), max(seat_ids)):
        if sid not in seat_ids and sid+1 in seat_ids and sid-1 in seat_ids:
            print(sid)
            break
    pass

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
