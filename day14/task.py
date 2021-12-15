import math
from collections import defaultdict


def parse_file():
    with open('day14/input.txt') as fp:
        template = fp.readline().strip()
        pair_insertions = {}
        for line in fp:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(' -> ', 1)
            pair_insertions[key] = value
    return template, pair_insertions


def solve(template, pair_insertions, steps=1):
    """Solves task counting two-letters words
    Example:
        template: KNO

        pair_insertions:
          - KN -> N
          - NN -> K
          - NO -> N
          - NK -> O

        Steps:
        Step 1. We know that KN always results in KN and NN,
        so we can take the number of KN from previous result
        and add it to both combinations
        NO -> NN and NO
        result -> {KN: 1, NN: 2, NO: 1}

        Step 2.
        Go through previous result
        KN -> KN and NN
        result -> {KN: prev[KN] or 1, NN: prev[KN] or 1}
        NN -> NK and KN
        result -> {KN: 1 + prev[NN], NN: 1, NK: prev[NN]}
               -> {KN: 3, NN: 1, NK: 2}
        ...
    Then we rebuild two-letters words to our needed one-letter words
    by dividing every count by 2
    (cause we count every letter twice in different combination)
    """

    counter = defaultdict(int)
    for first, second in zip(template, template[1:]):
        pair = first + second
        mid = pair_insertions[pair]
        counter[first + mid] += 1
        counter[mid + second] += 1

    steps -= 1
    for _ in range(steps):
        prev_counter = counter
        counter = defaultdict(int)
        for first, second in prev_counter:
            pair = first + second
            mid = pair_insertions[pair]
            counter[first + mid] += prev_counter[pair]
            counter[mid + second] += prev_counter[pair]

    new_counter = defaultdict(int)
    for (first, second), count in counter.items():
        new_counter[first] += count
        new_counter[second] += count
    for key, count in new_counter.items():
        new_counter[key] = math.ceil(count / 2)
    return max(new_counter.values()) - min(new_counter.values())


def solve_task1():
    template, pair_insertions = parse_file()
    return solve(template, pair_insertions, 10)


def solve_task2():
    template, pair_insertions = parse_file()
    return solve(template, pair_insertions, 40)


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
