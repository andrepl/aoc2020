import itertools
import math
from collections import defaultdict
from itertools import zip_longest
from operator import itemgetter

from timeit import timeit


LINES = [l.strip() for l in open('day21.txt').readlines()]

def get_allergens():
    data = {}
    all_ingredients = []

    for line in LINES:
        ingredients, allergens = line.split(' (contains ')
        allergens = allergens[:-1]
        ingredients = ingredients.split(' ')
        all_ingredients.extend(ingredients)
        ingredients = set(ingredients)

        allergens = allergens.split(', ')
        for a in allergens:
            if a not in data:
                data[a] = set(ingredients)
            else:
                data[a] = data[a].intersection(set(ingredients))

    print(data)
    taken = {}
    while data:
        for k, v in list(data.items()):
            if len(v) == 1:
                val = v.pop()
                taken[k] = val
                for v2 in data.values():
                    if val in v2:
                        v2.remove(val)
                del data[k]

    safe = defaultdict(int)
    for i in all_ingredients:
        if  i not in taken.values():
            safe[i] += 1

    return taken, safe


def part1():
   taken, safe = get_allergens()
   print(sum(safe.values()))


def part2():
    taken, safe = get_allergens()
    items = list(taken.items())
    items = sorted(items, key=itemgetter(0))
    print(','.join(i[1] for i in items))


if __name__ == '__main__':
    print("Part 1: ", end="")
    print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
