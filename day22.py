import functools
from timeit import timeit


p1raw, p2raw = open('day22.txt').read().split('\n\n')

P1DECK = [int(x) for x in p1raw.splitlines()[1:]]
P2DECK = [int(x) for x in p2raw.splitlines()[1:]]

gamenum = 0

def part1():
    p1deck = list(P1DECK)
    p2deck = list(P2DECK)
    while p1deck and p2deck:
        p1card, p2card = p1deck.pop(0), p2deck.pop(0)
        if p1card > p2card:
            p1deck.append(p1card)
            p1deck.append(p2card)
        elif p2card > p1card:
            p2deck.append(p2card)
            p2deck.append(p1card)
        else:
            print("WHOA BESSY")

    hands = sorted([p1deck, p2deck], key=lambda l: len(l))
    winner = hands[1]
    score = sum([a * b for a, b in zip(winner, reversed(range(1, len(winner) + 1)))])
    print(score)


@functools.lru_cache(maxsize=100000)
def playcombat(p1deck, p2deck):
    global gamenum
    gamenum += 1
    gid = gamenum

    seen = set()

    round = 0
    while p1deck and p2deck:
        round += 1
        # print('Round {} Game {}:'.format(round, gid))
        # print("Player 1's Deck: {}".format(p1deck))
        # print("Player 2's Deck: {}".format(p2deck))

        if (p1deck, p2deck) in seen:
            return p1deck, p2deck, 0

        seen.add((p1deck, p2deck))

        p1card, p1deck = p1deck[0], p1deck[1:]
        p2card, p2deck = p2deck[0], p2deck[1:]

        # print("Player 1 plays: {}".format(p1card))
        # print("Player 2 plays: {}".format(p2card))


        if len(p1deck) >= p1card and len(p2deck) >= p2card:
            # print("Playing a sub-game to determine the winner")
            p1sub, p2sub, winner = playcombat(p1deck[:p1card], p2deck[:p2card])
            # print("... anyway, back to game {}".format(gid))
        else:
            winner = 0 if p1card > p2card else 1
        # print("Player {} Wins Round {} of Game {}".format(winner+1, round, gid))

        if winner == 0:
            p1deck += (p1card, p2card)
        elif winner == 1:
            p2deck += (p2card, p1card)
        else:
            print("WHOA BESSY")
    gamewinner = int(len(p2deck) > len(p1deck))
    if gid % 1000 == 0:
        print("Game #{}".format(gid))
    # print("Player {} wins game {}".format(gamewinner, gid))
    return p1deck, p2deck, gamewinner

def part2():

    p1deck = tuple(P1DECK)
    p2deck = tuple(P2DECK)

    d1, d2, winner = playcombat(p1deck, p2deck)

    winner = [d1, d2][winner]
    score = sum([a * b for a, b in zip(winner, reversed(range(1, len(winner) + 1)))])
    print(score)



if __name__ == '__main__':
    print("Part 1: ", end="")
   # print("- Time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("- Time: ", timeit(part2, number=1))
