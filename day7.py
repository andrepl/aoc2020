from collections import defaultdict
from timeit import timeit
import re

# parse the input into...
# { 'posh crimson': [('mirrored tan', 2), ('faded red', 1), ('striped gray', 1)],
#   'bright gray': [('striped white', 1), ('vibrant cyan', 4), ('clear white', 4), ('muted gold', 4)]
#   ... }

MAP = defaultdict(list)
for line in open('day7.txt').readlines():
    container, contents = line.strip('.').split(' bags contain ')
    for c in contents.split(', '):
        if c == 'no other bags':
            continue
        m = re.match(r'(\d+)\s(\w+\s\w+)\sbags?', c)
        MAP[container].append((m.groups()[1], int(m.groups()[0])))


def part1():

    def can_hold(b):
        '''
        yield every bag that can directly hold the given bag `b`

        '''
        for k, contents in MAP.items():
            if b in (c[0] for c in contents):
                yield k

    # do an exhaustive BFS
    q = [('shiny gold', 1)]
    visited = set()

    # while the queue is not empty
    while q:
        # get the first node in the queue
        bag, score = q.pop(0)
        # find all bag colors that could directly hold this bag
        for parent in can_hold(bag):
            # if you've not visited this bag before, add it to the queue, and the visited set.
            if parent not in visited:
                visited.add(parent)
                q.append((parent, score + 1))

    # The result is the size of the visited queue.
    print(len(visited))


def part2():

    def get_cost(bag):
        '''
        recursively calculate the contents of a bag, plus 1 for the bag itself.

        '''
        return 1 + sum(get_cost(a) * b for a, b in MAP[bag])

    print(get_cost('shiny gold') - 1)  # the original bag doesn't count. -1


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
