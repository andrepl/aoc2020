import itertools
import time
from timeit import timeit

LINES = [list(l.strip()) for l in open('day11.txt').readlines()]
w, h = len(LINES[0]), len(LINES)


def nbrs(x, y, lines):
    nbrct = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < w and 0 <= ny < h:
                if (nx, ny) != (x, y) and lines[ny][nx] != '.':
                    nbrct +=  1 if lines[ny][nx] == '#' else 0
    return nbrct


def iterseats(ctr, lim, lines):
    flip = set()
    for y, line in enumerate(lines):
        for x, bit in enumerate(line):
            if bit == '.':
                continue
            nbrct = ctr(x, y, lines)
            if nbrct == 0 and bit == 'L':
                flip.add((x, y))
            elif nbrct >= lim and bit == '#':
                flip.add((x, y))

    for x, y in flip:
        lines[y][x] = '#' if lines[y][x] == 'L' else 'L'
    return flip


def part1():
    lines = [list(l) for l in LINES]

    lastflip = True
    iters = 0
    while lastflip:
        lastflip = iterseats(nbrs, 4, lines)
        iters += 1

    for line in lines:
        print(''.join(line))
    print('--')
    print(sum(l.count('#') for l in lines))

# copy these here because lazy

def vis(x, y, lines):
    visible = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (dx, dy) == (0, 0):
                continue
            for dist in range(1,max(w,h)+1):
                nx = x + (dx * dist)
                ny = y + (dy * dist)
                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    break
                if lines[ny][nx] == '#':
                    visible += 1
                    break
                elif lines[ny][nx] == 'L':
                    break
    return visible


def part2():
    print()
    lastflip = True
    iters = 0
    lines = [list(l) for l in LINES]

    while lastflip:
        lastflip = iterseats(vis, 5, lines)
        iters += 1

        # for line in lines:
        #     print(''.join(line))
        # print('--')
        # time.sleep(0.1)
    for line in lines:
        print(''.join(line))
    print('--')
    print(sum(l.count('#') for l in lines))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
