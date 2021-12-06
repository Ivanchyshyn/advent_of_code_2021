
def make_fishes(max_days=80):
    with open('day6/input.txt') as fp:
        fishes = list(
            map(int, fp.read().strip().split(','))
        )
    days = 0
    # Days from 0 to 8
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in fishes:
        result[fish] += 1
    while days != max_days:
        first = result[0]
        # move fish by 1 day
        for i in range(1, 9):
            result[i-1] = result[i]
        # Fish with 8 days -> the same as fish with 0 days
        result[-1] = first
        # 0 days fish move to 6 days
        result[6] += first
        days += 1
    return sum(result)


def solve_task1():
    return make_fishes()


def solve_task2():
    return make_fishes(max_days=256)


if __name__ == '__main__':
    result1 = solve_task1()
    result2 = solve_task2()
    print('task 1 -', result1)
    print('task 2 -', result2)
