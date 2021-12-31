from functions import (
    inp, add, mul, div, mod, eql,
)

INSTRUCTION_TO_ACTION = {
    'inp': inp,
    'add': add,
    'mul': mul,
    'div': div,
    'mod': mod,
    'eql': eql,
}


def parse_input():
    with open('day24/input.txt') as fp:
        return fp.read().strip().split('\n')


def get_initial_variables():
    return {
        'x': 0,
        'y': 0,
        'z': 0,
        'w': 0,
    }


def get_new_number(number):
    if number < 11_111_111_111_111:
        raise ValueError('No new number found')

    while True:
        number -= 1
        val = str(number)
        index = val.find('0')
        if index == -1:
            break
        left = val[index:]
        number -= int(left)
    return number


def solve_task1():
    instructions = parse_input()
    not_found = True
    number = 99_999_999_999_999
    while not_found:
        variables = get_initial_variables()
        values = iter(str(number))
        for instruction in instructions:
            func, code = instruction.split(maxsplit=1)
            if func == 'inp':
                inp(code, variables, next(values))
            else:
                INSTRUCTION_TO_ACTION[func](code, variables)
        if variables['z'] == 0:
            not_found = False
        else:
            number = get_new_number(number)
    return number


def solve_task2():
    return


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
