from pprint import pprint


def get_points_and_fold_along():
    points = set()
    fold_along = []

    with open('day13/input.txt') as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            elif line.startswith('fold along'):
                line = line[len('fold along'):].strip()
                axis, value = line.split('=', 1)
                fold_along.append((axis, int(value)))
            else:
                x, y = line.split(',')
                points.add((int(x), int(y)))
    return points, fold_along


def count_dots(grid):
    return sum(value == '#' for row in grid for value in row)


def fold_paper(points, fold_along):
    max_x = max_y = 0
    for x, y in points:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    grid = [
        [
            '#' if (x, y) in points else '.'
            for x in range(max_x + 1)
        ]
        for y in range(max_y + 1)
    ]

    for fold_direction, fold_value in fold_along:
        if fold_direction == 'y':
            # Second half of folded paper can be smaller
            # So we need figure out where to start from
            # so that the segments are equal in length
            start_count = abs(fold_value * 2 - max_y)
            for y, reverse_y in enumerate(range(max_y, fold_value, -1), start_count):
                for x in range(max_x + 1):
                    if grid[reverse_y][x] == '#':
                        grid[y][x] = '#'
            grid = grid[:fold_value]
            max_y = fold_value - 1
        else:
            start_count = abs(fold_value * 2 - max_x)
            for row in grid:
                for x, reverse_x in enumerate(range(max_x, fold_value, -1), start_count):
                    if row[reverse_x] == '#':
                        row[x] = '#'
                row[:] = row[:fold_value]
            max_x = fold_value - 1
        yield grid


def solve_task1():
    points, fold_along = get_points_and_fold_along()
    grid = next(fold_paper(points, fold_along))
    return count_dots(grid)


def solve_task2():
    points, fold_along = get_points_and_fold_along()
    grid = []
    for grid in fold_paper(points, fold_along):
        pass
    return grid


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -')
    for _row in result2:
        print(_row)
