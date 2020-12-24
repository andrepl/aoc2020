import re
from collections import defaultdict
from timeit import timeit


lines = [l.strip() for l in open('day24.txt').readlines()]


STEPS = dict(
    e=(1, -1, 0),
    w=(-1, 1, 0),
    ne=(1, 0, -1),
    nw=(0, 1, -1),
    se=(0, -1, 1),
    sw=(-1, 0, 1)
)

grid = defaultdict(bool)


def part1():
    for l in lines:
        x, y, z = 0, 0, 0
        while l:
            if l[0] in 'ns':
                step, l = l[:2], l[2:]
            else:
                step, l = l[:1], l[1:]
            dx, dy, dz = STEPS[step]
            x += dx
            y += dy
            z += dz
        grid[(x, y, z)] = not grid[(x, y, z)]
    print(len([v for v in grid.values() if v]))
    print(grid)


def get_black_neighbours(pt):
    x,y,z = pt
    for dx, dy, dz in STEPS.values():
        nbr = (x + dx, y + dy, z + dz)
        if grid[nbr]:
            yield nbr


def play_gol():
    toflip = set()
    for coords, tile in list(grid.items()):
        nbrs = list(get_black_neighbours(coords))
        if tile and (len(nbrs) == 0 or len(nbrs) > 2):
            toflip.add(coords)
        elif (not tile) and len(nbrs) == 2:
            toflip.add(coords)

    for coords in toflip:
        grid[coords] = not grid[coords]


def part2():
    for k, v in grid.items():
        if v:
            print(k)


    for i in range(100):
        play_gol()
        print("Day {}: {}".format(i, len([v for v in grid.values() if v])))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
