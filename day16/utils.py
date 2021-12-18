import operator
from functools import reduce


def sum_(*args):
    if len(args) == 1:
        args = args[0]
    return sum(args)


def multiply(*args):
    if not args:
        return 0
    if len(args) == 1:
        args = args[0]
    return reduce(operator.mul, args, 1)


def min_(*args):
    if not args:
        return 0
    if len(args) == 1:
        args = args[0]
    return min(args)


def max_(*args):
    if not args:
        return 0
    if len(args) == 1:
        args = args[0]
    return max(args)


def gt_(*args):
    if not args:
        return 0
    if len(args) == 1:
        args = args[0]
    return operator.gt(*args)


def lt_(*args):
    if not args:
        return 0
    if len(args) == 1:
        args = args[0]
    return operator.lt(*args)


def eq_(*args):
    if not args:
        return 0
    if len(args) == 1:
        args = args[0]
    return operator.eq(*args)


TYPE_TO_OPERATION = {
    0: sum_,
    1: multiply,
    2: min_,
    3: max_,
    5: gt_,
    6: lt_,
    7: eq_,
}
