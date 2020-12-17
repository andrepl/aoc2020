from collections import defaultdict
from operator import itemgetter
from timeit import timeit

LINES = [l.strip() for l in open('day17.txt').readlines()]


def load_initial_state():
    space = defaultdict(int)
    for y, line in enumerate(LINES):
        for x, char in enumerate(line):
            space[(x-1, y-1, 0)] = 1 if char == '#' else 0
    return space


def load_initial_state4d():
    space = defaultdict(int)
    for y, line in enumerate(LINES):
        for x, char in enumerate(line):
            space[(x-1, y-1, 0, 0)] = 1 if char == '#' else 0
    return space


def get_active_neighbours(pt, space):
    count = 0
    _x, _y, _z = pt
    for y in (-1, 0, 1):
        for x in (-1, 0, 1):
            for z in (-1, 0, 1):
                if x == 0 and y == 0 and z == 0: continue
                count += space[(x + _x, y + _y, z + _z)]
    return count


def get_active_neighbours4d(pt, space):
    count = 0
    _x, _y, _z, _w = pt
    for w in (-1, 0, 1):
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                for z in (-1, 0, 1):
                    if x == 0 and y == 0 and z == 0 and w == 0: continue
                    count += space[(x + _x, y + _y, z + _z, w + _w)]
    return count


def tick(space):
    flip = []

    xkeys = sorted(space.keys(), key=itemgetter(0))
    ykeys = sorted(space.keys(), key=itemgetter(1))
    zkeys = sorted(space.keys(), key=itemgetter(2))
    # print(space)
    for z in range(zkeys[0][2]-1, zkeys[-1][2]+2):
        for y in range(ykeys[0][1]-1, ykeys[-1][1]+2):
            for x in range(xkeys[0][0]-1, xkeys[-1][0]+2):
                pt = (x, y, z)
                val = space[(x, y, z)]
                neighbour_count = get_active_neighbours(pt, space)
                if val and neighbour_count not in (2, 3):
                    flip.append(pt)
                elif not val and neighbour_count == 3:
                    flip.append(pt)

    for pt in flip:
        space[pt] = 0 if space[pt] else 1
    return space


def tick4d(space):
    flip = []

    xkeys = sorted(space.keys(), key=itemgetter(0))
    ykeys = sorted(space.keys(), key=itemgetter(1))
    zkeys = sorted(space.keys(), key=itemgetter(2))
    wkeys = sorted(space.keys(), key=itemgetter(3))

    for w in range(wkeys[0][3]-1, wkeys[-1][3]+2):
        for z in range(zkeys[0][2]-1, zkeys[-1][2]+2):
            for y in range(ykeys[0][1]-1, ykeys[-1][1]+2):
                for x in range(xkeys[0][0]-1, xkeys[-1][0]+2):
                    pt = (x, y, z, w)
                    val = space[(x, y, z, w)]
                    neighbour_count = get_active_neighbours4d(pt, space)
                    if val and neighbour_count not in (2, 3):
                        flip.append(pt)
                    elif not val and neighbour_count == 3:
                        flip.append(pt)

    for pt in flip:
        space[pt] = 0 if space[pt] else 1
    return space


def part1():
    space = load_initial_state()
    for i in range(6):
        space = tick(space)
    print(sum(space.values()))


def part2():
    space = load_initial_state4d()
    for i in range(6):
        space = tick4d(space)
    print(sum(space.values()))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
