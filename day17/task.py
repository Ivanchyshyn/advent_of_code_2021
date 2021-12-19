import math
import re

PATTERN = re.compile(
    r'x=(?P<x>-?\d+\.\.-?\d+).*?y=(?P<y>-?\d+\.\.-?\d+)'
)


def parse_input():
    with open('day17/input.txt') as fp:
        line = fp.read().strip()
    res = PATTERN.search(line)
    x, y = res.group('x'), res.group('y')

    x = tuple(map(int, x.split('..')))
    y = tuple(map(int, y.split('..')))
    return x, y


def get_height(y, velocity):
    y += velocity * (velocity + 1) // 2
    return y


def find_root(c):
    """Find arithmetic sum
    S = n * (n + 1) / 2
    n^2 + n = 2 * S
    n^2 + n - (2 * S) = 0
    Solve quadratic equation
    """
    a = b = 1
    c = -(2 * c)
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))
    if dis_form > 0:
        res = (-b + sqrt_val) / (2 * a)
        if res > 0 and res.is_integer():
            return int(res)


def get_row_constraints(col_area):
    min_x = 0
    max_x = col_area[0]
    for i in range(col_area[0], col_area[1] + 1):
        root = find_root(i)
        if root is not None:
            min_x = root
            break
    return min_x, max_x


def solve_task1():
    """Max height can be reached if we take the lowest y-point
    and set that it's last y-velocity went from 0 to it.
    So, y-velocity = absolute y-point.
    Then, we find arithmetic sum of y-velocity (n):
    0 + 1 + .. + n - 1 + n = n * (n + 1) // 2
    Then find the highest y by adding the sum to lowest y-point
    """
    col_area, row_area = parse_input()
    return get_height(row_area[0], abs(row_area[0]))


def solve_task2():
    def is_valid(x, y, times):
        """Check if shoot connects to target"""

        if (x, y) in seen:
            return True
        if (
            col_area[0] <= x <= col_area[-1]
            and row_area[0] <= y <= row_area[-1]
        ):
            return True
        if x > col_area[-1] or y < row_area[0]:
            return False

        if times[0] != 0:
            time_x = times[0] - 1
            x += time_x
        else:
            time_x = 0

        time_y = times[1] - 1
        y += time_y
        new_times = time_x, time_y
        return is_valid(x, y, new_times)

    col_area, row_area = parse_input()
    # Starts directly within the target
    total = (
        (col_area[1] - col_area[0] + 1)
        * (row_area[1] - row_area[0] + 1)
    )
    min_x, max_x = get_row_constraints(col_area)

    max_height = get_height(row_area[0], abs(row_area[0]))
    min_y = row_area[1]
    max_y = find_root(max_height)

    seen = set()
    # Bruteforce check all points from lowest to highest
    for i in range(min_x, max_x):
        for j in range(max_y, min_y, -1):
            if is_valid(i, j, (i, j)):
                seen.add((i, j))
    return total + len(seen)


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
