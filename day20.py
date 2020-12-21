import itertools
import math
from itertools import zip_longest

from timeit import timeit


TILESTRS = [l.strip() for l in open('day20.txt').read().split('\n\n')]
ROT = str.maketrans({'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'})
XFLIP = str.maketrans({'N': 'S', 'S': 'N'})
YFLIP = str.maketrans({'W': 'E', 'E': 'W'})


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


class Tile:

    SEAMONSTER_SHAPE = [
        (0, 0),
        (-18, 1), (-13, 1), (-12, 1), (-7, 1), (-6, 1), (-1, 1), (0, 1), (1, 1),
        (-17, 2), (-14, 2), (-11, 2), (-8, 2), (-5, 2), (-2, 2)
    ]

    def __init__(self, tile_id, src, orientation=0, flipped_x=False, flipped_y=False, blank_edges=''):
        self._src = [l for l in src]
        self.id = tile_id
        self.orientation = orientation
        self.flipped_x = flipped_x
        self.flipped_y = flipped_y
        self.blank_edges = blank_edges

    def get_edges(self):
        return [
            self.get_edge('N'),
            self.get_edge('S'),
            self.get_edge('E'),
            self.get_edge('W'),
        ]

    def get_edge(self, direction):
        if direction == 'N':
            return self._src[0]
        elif direction == 'S':
            return self._src[-1]
        elif direction == 'E':
            return ''.join(l[-1] for l in self._src)
        elif direction == 'W':
            return ''.join(l[0] for l in self._src)

    def rotate(self):
        self._src = [''.join(tup) for tup in zip(*self._src[::-1])]
        self.orientation = (self.orientation + 1) % 4
        self.blank_edges = self.blank_edges.translate(ROT)

    def print(self):
        for line in self._src:
            print(line)

    def flipx(self):
        self._src = list(reversed(self._src))
        self.flipped_x = not self.flipped_x
        self.blank_edges = self.blank_edges.translate(XFLIP)

    def flipy(self):
        self._src = [''.join(list(reversed(l))) for l in self._src]
        self.flipped_y = not self.flipped_y
        self.blank_edges = self.blank_edges.translate(YFLIP)

    def could_match_edge(self, edge):
        for e in self.get_edges():
            if e == edge or ''.join(reversed(e)) == edge:
                return True
        return False

    def matches_edgereqs(self, edgereqs):
        for k, v in edgereqs.items():
            my_edge = self.get_edge(k)
            if v is None:  # edge must be blank
                if k not in self.blank_edges:
                    return False
            elif v not in (my_edge, ''.join(reversed(my_edge))):
                return False
        return True


    def clone(self):
        return Tile(self.id, self._src, self.orientation, self.flipped_x, self.flipped_y, self.blank_edges)

    def cropped_source(self):
        lines = []
        for y in range(1, len(self._src)-1):
            lines.append(self._src[y][1:-1])
        return lines

    def all_possible_orientations(self):
        t = self.clone()
        for i in range(8):
            t = t.clone()
            if i == 4:
                t.flipy()
            t.rotate()
            yield t

    def has_seamonster_at(self, x, y):
        for _x, _y in self.SEAMONSTER_SHAPE:
            if self._src[_y + y][_x + x] != '#':
                return False
        return True

    def find_seamonsters(self):
        locations = []
        for y in range(len(self._src)-3):
            for x in range(18, len(self._src[0])-1):
                if self.has_seamonster_at(x, y):
                    locations.append((x, y))
        return locations

    def erase_monsters(self, monsters):
        grid = [list(l) for l in self._src]
        for x, y in monsters:
            for _x, _y in self.SEAMONSTER_SHAPE:
                grid[y+_y][x+_x] = '.'
        self._src = [''.join(l) for l in grid]

    def count_hashes(self):
        count = 0
        for line in self._src:
            for char in line:
                if char == '#':
                    count += 1
        return count


def parse_input():
    tiles = dict()
    for tsrc in TILESTRS:
        tsrc = tsrc.splitlines()
        label, src = tsrc[0], tsrc[1:]
        tid = int(label[5:-1])
        tiles[tid] = Tile(tid, src)

    for tile in tiles.values():
        others = [t for t in tiles.values() if t.id != tile.id]
        tile.blank_edges = ''
        for direction in 'NESW':
            edge = tile.get_edge(direction)
            if not any(o for o in others if o.could_match_edge(edge)):
                tile.blank_edges += direction

    return tiles


def part1():
    tiles = parse_input()
    print(math.prod(t.id for t in tiles.values() if len(t.blank_edges) == 2))


def find_matching_tile(tiles_list, edgereqs):
    for t in tiles_list:
        for o in t.all_possible_orientations():
            if o.matches_edgereqs(edgereqs):
                return o


def assemble_puzzle(tiles):
    tiles_list = list(tiles.values())
    dim = int(math.sqrt(len(tiles)))
    grid = dict.fromkeys(itertools.permutations(range(dim), 2))  # initialize an empty grid

    # pick any corner piece and put it at 0, 0
    grid[(0, 0)] = [t for t in tiles_list if len(t.blank_edges) == 2][0]

    # the rest of part 2 wants the data as a list rather than the dict we use here.
    # it's easier to build it up as we go than to do it all at the end.
    grid_as_list = [grid[(0, 0)]]


    # remove that corner from the tiles_list this is our 'pool' of remaining usable tiles.
    tiles_list.remove(grid[(0, 0)])

    # Rotate the initial corner piece correctly
    while grid[(0, 0)].blank_edges not in ('NW', 'WN'):
        grid[(0, 0)].rotate()
        print(grid[(0, 0)].blank_edges)

    # fill it all in.  We do this by building up a dict of 'edge requirements'
    # which maps a cardinal direction (N, S, E, W) to either None (no neighbouring tile)
    # or a string representation of the pattern that must exist on that edge.

    # Then every remaining tile -- in all 8 orientations -- is tested using the
    # Tile.matches_edgereqs method to check if it meets all the requirements.

    for y in range(dim):
        for x in range(dim):
            if x == 0 and y == 0: continue
            edgereqs = {}

            # Nones in edgereqs signify that the edge must be a 'blank' edge
            if y == 0:
                edgereqs['N'] = None
            elif y == dim-1:
                edgereqs['S'] = None

            if x == 0:
                edgereqs['W'] = None
            elif x == dim-1:
                edgereqs['E'] = None

            # Use the tiles to the west and/or north of the current spot as edge requirements
            if y > 0:
                edgereqs['N'] = grid[(x, y-1)].get_edge('S')
            if x > 0:
                edgereqs['W'] = grid[(x-1, y)].get_edge('E')

            # There's only ever 1 tile that fits the requirements.
            tile = find_matching_tile(tiles_list, edgereqs)
            grid[(x, y)] = tile
            grid_as_list.append(tile)

            # Remove it from the tiles_list, it's been used.
            tiles_list = [t for t in tiles_list if t.id != tile.id]

    return grid_as_list


def part2():
    print()
    tiles = parse_input()

    tiles_list = assemble_puzzle(tiles)

    ## Solve Part 2

    # dim is the length of one side of the square grid
    dim = int(math.sqrt(len(tiles_list)))

    # The stitched together image lines
    newlines = []

    # Do the stitching together of the tiles into one big tile.
    # Dont think too hard about it...
    for row in grouper(tiles_list, dim):
        sources = [i.cropped_source() for i in row]
        for lines in zip(*sources):
            newlines.append(''.join(lines))
    image = Tile(0, newlines)

    # Keep flipping and rotating until we find sea monsters.
    for image in image.all_possible_orientations():
        monsters = image.find_seamonsters()
        if monsters:
            # this isn't the best way to do this, but hey.
            image.erase_monsters(monsters)
            print(image.count_hashes())


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
