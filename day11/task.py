
def get_grid():
    grid = []
    with open('day11/input.txt') as fp:
        for line in fp:
            grid.append(list(map(int, line.strip())))
    return grid


def valid_surrounding(grid, i, j):
    checks = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
    ]
    rows, cols = len(grid), len(grid[0])
    for x, y in checks:
        if 0 <= x < rows and 0 <= y < cols:
            yield x, y


def recursion(grid, i, j, flashes):
    newly = []
    for x, y in valid_surrounding(grid, i, j):
        if (x, y) in flashes:
            continue

        num = grid[x][y]
        if num == 9:
            grid[x][y] = 0
            newly.append((x, y))
        else:
            grid[x][y] += 1
    flashes.update(newly)
    return sum(1 + recursion(grid, x, y, flashes) for x, y in newly)


def flash_energy(grid, steps=None):
    step = 0
    while step != steps:
        results = []
        flashes = set()
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if (i, j) in flashes:
                    continue
                if num == 9:
                    row[j] = 0
                    flashes.add((i, j))
                    results.append(1 + recursion(grid, i, j, flashes))
                else:
                    row[j] += 1
        step += 1
        yield results, flashes


def solve_task1():
    grid = get_grid()
    total = 0
    for results, _ in flash_energy(grid, steps=100):
        total += sum(results)
    return total


def solve_task2():
    grid = get_grid()
    step = 0
    # All indexes should flash
    all_flashes = {(x, y) for x in range(10) for y in range(10)}
    for _, flashes in flash_energy(grid):
        step += 1
        if flashes == all_flashes:
            break

    return step


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
