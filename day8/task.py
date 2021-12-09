import itertools


def solve_task1():
    output_values = []
    unique_length = (
        2, 3, 4, 7,
    )
    with open('day8/input.txt') as fp:
        for line in fp:
            values = line.split('|', 1)[1].strip()
            output_values.append(values.split())
    return sum(
        len(value) in unique_length
        for values in output_values
        for value in values
    )


"""
Indexes in valid combinations
 0000
1    2
1    2
 3333
4    5
4    5
 6666
"""
valid_combinations = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 0, 1): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9,
}


def solve_task2():
    patterns, outputs = [], []
    with open('day8/input.txt') as fp:
        for line in fp:
            pattern, output = line.split('|', 1)
            patterns.append(pattern.strip().split())
            outputs.append(output.strip().split())

    actual_combinations = []
    for pattern, output in zip(patterns, outputs):
        found_output = []
        for value in output:
            if len(value) == 2:
                found_output.append(1)
            elif len(value) == 3:
                found_output.append(7)
            elif len(value) == 4:
                found_output.append(4)
            elif len(value) == 7:
                found_output.append(8)
            else:
                found_output.append(set(value))

        result = [[] for _ in range(1, 6)]
        for value in pattern:
            if len(value) == 7:
                # this doesn't make any difference - continue
                continue
            value = set(value)
            temp = result[len(value) - 2]
            if value in temp:
                continue
            temp.append(value)

        values = [0] * 7
        possible_combinations = set()
        recursion(result, values, 0, possible_combinations)
        for comb in possible_combinations:
            temp = found_output[:]
            for index, found in enumerate(temp):
                if not isinstance(found, set):
                    continue
                valid = check_combination(comb, found)
                if valid is None:
                    break
                temp[index] = valid
            else:
                found_output = temp
                break
        # [1, 2, 3, 4] -> 1234
        num = 0
        for n in found_output:
            num = num * 10 + n
        actual_combinations.append(num)

    return sum(actual_combinations)


def recursion(result, values, i, possible_combinations):
    if i == 5:
        possible_combinations.add(tuple(values))
        return
    if not result[i]:
        return recursion(result, values, i + 1, possible_combinations)

    if i == 0:
        can_fill_indexes = {2, 5}
        need_to_check_indexes = ()
    elif i == 1:
        can_fill_indexes = {0, 2, 5}
        need_to_check_indexes = (2, 5)
    # Four letters
    elif i == 2:
        can_fill_indexes = {1, 2, 3, 5}
        need_to_check_indexes = (0, 2, 5)
    else:
        # Five and six letters need to try everywhere
        can_fill_indexes = set(range(7))
        need_to_check_indexes = list(range(7))

    for letters in result[i]:
        filled_indexes = set()
        filled_letter = set()
        for index in need_to_check_indexes:
            if values[index]:
                filled_indexes.add(index)
                filled_letter.add(values[index])
        not_filled_letter = letters - filled_letter
        not_filled_indexes = can_fill_indexes - filled_indexes
        for perm in itertools.permutations(not_filled_letter):
            for index, value in zip(not_filled_indexes, perm):
                values[index] = value
            recursion(result, values, i + 1, possible_combinations)
            for index in not_filled_indexes:
                values[index] = 0


def get_num_from_combination(values):
    for comb in valid_combinations:
        if all(bool(val) == checked for val, checked in zip(values, comb)):
            return valid_combinations[comb]
    return None


def check_combination(comb, output):
    values = [0] * 7
    for letter in output:
        if letter not in comb:
            return None
        values[comb.index(letter)] = letter
    return get_num_from_combination(values)


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
