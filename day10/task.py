
OPEN_TO_CLOSE = dict(zip('([{<', ')]}>'))
CORRUPTED_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
NOT_COMPLETED_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def go_through_chunks(chunks):
    """Generator, that goes through chunks of brackets.
    Checks if opening bracket has it's matching closing bracket.
    :returns tuple of
      - (invalid char, False) if found invalid closing bracket
      - (remaining que, True) if no invalid closing brackets found
    """

    for chunk in chunks:
        que = []
        for char in chunk:
            if char in OPEN_TO_CLOSE:
                que.append(char)
            elif not que:
                yield char, False
                break
            else:
                open_char = que.pop()
                if OPEN_TO_CLOSE[open_char] != char:
                    yield char, False
                    break
        else:
            yield que, True


def solve_task1():
    with open('day10/input.txt') as fp:
        chunks = fp.read().split('\n')

    invalid = []
    for value, is_valid in go_through_chunks(chunks):
        if not is_valid:
            invalid.append(value)
    return sum(CORRUPTED_SCORES[char] for char in invalid)


def solve_task2():
    with open('day10/input.txt') as fp:
        chunks = fp.read().split('\n')

    incomplete = []
    for value, is_valid in go_through_chunks(chunks):
        if not is_valid:
            continue

        if value:
            incomplete.append([
                OPEN_TO_CLOSE[char] for char in reversed(value)
            ])
    totals = []
    for que in incomplete:
        total = 0
        for char in que:
            total *= 5
            total += NOT_COMPLETED_SCORES[char]
        totals.append(total)
    totals.sort()
    return totals[len(totals) // 2]


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
