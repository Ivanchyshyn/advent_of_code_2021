import itertools
from collections import defaultdict
from functools import lru_cache


def parse_input():
    with open('day21/input.txt') as fp:
        first = fp.readline()
        second = fp.readline()
        first = int(first.split(': ', 1)[1].strip())
        second = int(second.split(': ', 1)[1].strip())
    return first, second


def get_position(position, steps):
    result = (position + steps) % 10
    if result == 0:
        result = 10
    return result


def solve_task1():
    first_pos, second_pos = parse_input()
    first_total = second_total = 0
    first_turn = True
    die_rolled = 0

    cycle = itertools.cycle(list(range(1, 101)))
    for die_rolled, rolls in enumerate(zip(cycle, cycle, cycle), 1):
        total = sum(rolls) % 10
        if first_turn:
            first_pos = get_position(first_pos, total)
            first_total += first_pos
        else:
            second_pos = get_position(second_pos, total)
            second_total += second_pos

        if first_total >= 1000 or second_total >= 1000:
            break

        first_turn = not first_turn

    if first_turn:
        looser = second_total
    else:
        looser = first_total
    return looser * die_rolled * 3


def dices():
    dice = defaultdict(int)
    for i in range(1, 4):
        for j in range(1, 4):
            for z in range(1, 4):
                total = i + j + z
                dice[total] += 1
    return dice


def solve_task2():
    @lru_cache(None)
    def recursion(pos1, total1, pos2, total2):
        if total1 >= 21:
            return 1, 0
        elif total2 >= 21:
            return 0, 1
        won1 = won2 = 0
        for steps, univ in dice.items():
            pos = get_position(pos1, steps)
            count2, count1 = recursion(pos2, total2, pos, total1 + pos)
            won1, won2 = won1 + univ * count1, won2 + univ * count2
        return won1, won2

    first_pos, second_pos = parse_input()
    dice = dices()
    return max(recursion(first_pos, 0, second_pos, 0))


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
