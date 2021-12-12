from collections import defaultdict


def get_caves_mapping():
    mapping = defaultdict(set)
    with open('day12/input.txt') as fp:
        for line in fp:
            start, finish = line.strip().split('-', 1)
            if finish == 'start':
                # Do not link to start
                mapping[finish].add(start)
            else:
                mapping[start].add(finish)
            if finish not in ('end', 'start') and start != 'start':
                # Make reverse link
                mapping[finish].add(start)
    return mapping


def recursion(mapping, value, result, current_path, can_have_second=True):
    if value == 'end':
        current_path.append(value)
        result.add(tuple(current_path))
        return

    last = current_path[-1]
    if last.isupper():
        # Can go back to previous big cave
        if value not in current_path:
            recursion(mapping, last, result, [*current_path, value], can_have_second)
        elif can_have_second:
            # Cna try taking smaller cave once
            recursion(mapping, last, result, [*current_path, value], False)

    current_path.append(value)
    for new_value in mapping[value]:
        if new_value.islower() and new_value in current_path:
            if can_have_second:
                recursion(mapping, new_value, result, current_path.copy(), False)
            continue
        recursion(mapping, new_value, result, current_path.copy(), can_have_second)


def solve_task1():
    mapping = get_caves_mapping()
    result = set()
    for value in mapping.get('start', []):
        recursion(mapping, value, result, ['start'], False)
    return len(result)


def solve_task2():
    mapping = get_caves_mapping()
    result = set()
    for value in mapping.get('start', []):
        recursion(mapping, value, result, ['start'])
    return len(result)


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
