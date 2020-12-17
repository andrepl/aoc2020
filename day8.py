from collections import defaultdict
from timeit import timeit
import re

instructions = [l.strip() for l in open('day8.txt').readlines()]


class Program:
    def __init__(self, _instructions):
        self.acc = 0
        self.ptr = 0
        self.code = [(a.split(' ')[0], int(a.split(' ')[1])) for a in _instructions]
        print(self.code)
        self.history = []
        self.looped = False

    def exec(self):
        ins, arg = self.code[self.ptr]
        print(ins, arg)
        if self.ptr in self.history:
            self.looped = True
            print("looped with acc {}".format(self.acc))
            return True
        self.history.append(self.ptr)

        if ins == 'jmp':
            self.ptr += arg
        elif ins == 'acc':
            self.acc += arg
            self.ptr += 1
        elif ins == 'nop':
            self.ptr += 1
        if self.ptr == len(self.code):
            print("exited successfully with acc {}".format(self.acc))
            return True

    def run_until_loop_or_exit(self):
        ret = None
        while ret is None:
            ret = self.exec()


def part1():
    pass
    p = Program(instructions)
    ret = None
    while ret is None:
        ret = p.exec()



def part2():
    # find all progam variants
    prog_vars = []
    for i in range(len(instructions)):
        beforecode = instructions[:i]
        aftercode = instructions[i+1:]
        new_ins = instructions[i]
        if instructions[i].startswith('jmp'):
            new_ins = 'nop {}'.format(instructions[i].split(' ')[1])
        elif instructions[i].startswith('nop'):
            new_ins = 'jmp {}'.format(instructions[i].split(' ')[1])
        if new_ins != instructions[i]:
            newcode = beforecode
            newcode.append(new_ins)
            newcode.extend(aftercode)
            prog_vars.append(newcode)

    # we now have every possible variant of the program, run them all until we find the good one

    for i, variant in enumerate(prog_vars):
        p = Program(variant)
        p.run_until_loop_or_exit()
        if not p.looped:
            print(p.acc)
            break

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
