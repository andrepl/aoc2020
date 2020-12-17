from collections import defaultdict
from timeit import timeit

CODE = [l.strip() for l in open('day14.txt').readlines()]
HALTED = object()


class Interpreter:
    def __init__(self, CODE):
        self.code = CODE
        self.ptr = 0
        self.mask = None
        self.mem = defaultdict(int)

    def run_once(self):
        instruction = self.code[self.ptr]
        print(instruction)
        lhs, rhs = instruction.split(' = ')
        if lhs == 'mask':
            self.mask = rhs
        elif lhs.startswith('mem['):
            addr = int(lhs[4:-1])
            self.write_mem(addr, int(rhs))
        self.ptr += 1
        return self.ptr < len(self.code)

    def apply_mask(self, val):
        valbin = bin(val)[2:].rjust(36, '0')
        res = ''
        for maskbit, valbit in zip(self.mask, valbin):
            if maskbit == 'X':
                res += valbit
            else:
                res += maskbit
        return int(res, 2)

    def write_mem(self, addr, val):
        self.mem[addr] = self.apply_mask(val)


class Interpreter2(Interpreter):

    def apply_mask_floating(self, val):
        valbin = bin(val)[2:].rjust(36, '0')
        q = ['']
        while q:
            res = q.pop(0)
            for maskbit, valbit in zip(self.mask[len(res):], valbin[len(res):]):
                if maskbit == '0':
                    res += valbit
                elif maskbit == '1':
                    res += '1'
                else:  # X, floating
                    res += '0'
                    q.append(res[:-1] + '1')
            yield int(res, 2)

    def write_mem(self, addr, val):
        for addr in self.apply_mask_floating(addr):
            self.mem[addr] = val


def part1():
    i = Interpreter(CODE)
    while i.run_once():
        pass
    print(sum(i.mem.values()))


def part2():
    i = Interpreter2(CODE)
    res = None
    while i.run_once():
        pass
    print(i.mem)
    print(sum(i.mem.values()))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
