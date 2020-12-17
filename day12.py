import itertools
import math
import re
from timeit import timeit

INSTRUCTIONS = [l.strip() for l in open('day12.txt').readlines()]


class Ship:
    facing = 0
    pos = 0, 0

    def do(self, instruction):
        match = re.match(r'(\w)(\d+)', instruction)
        val = int(match.groups()[1])
        code = match.groups()[0]
        # forward is just another way of saying the cardinal direction you're facing.
        if code == 'F':
            code = self.get_facing_code()
        if code == 'R':
            self.facing += val
        elif code == 'L':
            self.facing -= val
        elif code == 'N':
            self.pos = (self.pos[0], self.pos[1] - val)
        elif code == 'S':
            self.pos = (self.pos[0], self.pos[1] + val)
        elif code == 'E':
            self.pos = (self.pos[0] + val, self.pos[1])
        elif code == 'W':
            self.pos = (self.pos[0] - val, self.pos[1])
        print(self.pos, self.get_facing_code())

    def get_facing_code(self):
        self.facing = abs(self.facing % 360)
        if self.facing == 0:
            return 'E'
        elif self.facing == 90:
            return 'S'
        elif self.facing == 180:
            return 'W'
        elif self.facing == 270:
            return 'N'



class Ship2:
    pos = 0, 0
    wp = 10, -1
    
    def do(self, instruction):
        match = re.match(r'(\w)(\d+)', instruction)
        val = int(match.groups()[1])
        code = match.groups()[0]

        if code == 'R':
            self.rotate_wp(val)
        elif code == 'L':
            self.rotate_wp(-val)
        elif code == 'N':
            self.wp = (self.wp[0], self.wp[1] - val)
        elif code == 'S':
            self.wp = (self.wp[0], self.wp[1] + val)
        elif code == 'E':
            self.wp = (self.wp[0] + val, self.wp[1])
        elif code == 'W':
            self.wp = (self.wp[0] - val, self.wp[1])
        elif code == 'F':
            dx, dy = self.wp[0] * val, self.wp[1] * val
            self.pos = (self.pos[0] + dx, self.pos[1] + dy)


    def rotate_wp(self, degrees):

        # decimals dont make sense here....
        # print('wpin', self.wp, degrees)
        # s = math.sin(math.radians(degrees))
        # c = math.cos(math.radians(degrees))
        # nx = int(math.floor(self.wp[0] * c - self.wp[1] * s))
        # ny = int(math.floor(self.wp[0] * s + self.wp[1] * c))
        if abs(degrees) == 180:
            self.wp = (-self.wp[0], -self.wp[1])
        elif degrees in (-90, 270):
            self.wp = (self.wp[1], -self.wp[0])
        elif degrees in (90, -270):
            self.wp = (-self.wp[1], self.wp[0])


        # print('wpout', self.wp)


def part1():
    ship = Ship()
    for i in INSTRUCTIONS:
        ship.do(i)
    print(abs(ship.pos[0]) + abs(ship.pos[1]))


def part2():
    ship = Ship2()
    for i in INSTRUCTIONS:
        ship.do(i)
        print(ship.pos, ship.wp)
    print(abs(ship.pos[0]) + abs(ship.pos[1]))



if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
