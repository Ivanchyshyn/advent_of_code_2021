def parse_input():
    with open('day20/input.txt') as fp:
        enhance = fp.readline().strip()
        image = [
            list(string)
            for string in fp.read().strip().split('\n')
        ]
    return enhance, image


def add_more_lines(image, times, outside='.'):
    rows, cols = len(image), len(image[0])
    new_image = []
    i = -times
    while i < rows + times:
        j = -times
        temp = []
        while j < cols + times:
            if 0 <= i < rows and 0 <= j < cols:
                temp.append(image[i][j])
            else:
                temp.append(outside)
            j += 1
        new_image.append(temp)
        i += 1
    return new_image


def get_neighbours(image, i, j, outside='.'):
    rows, cols = len(image), len(image[0])
    result = []
    for x, y in (
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1), (i, j), (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1),
    ):
        if 0 <= x < rows and 0 <= y < cols:
            result.append(image[x][y])
        else:
            result.append(outside)
    return ''.join('1' if char == '#' else '0' for char in result)


def solve(times):
    enhance, image = parse_input()
    outside = '.'
    for _ in range(times):
        image = add_more_lines(image, 3, outside)
        new_image = []
        for i, row in enumerate(image):
            temp = []
            for j, char in enumerate(row):
                result = get_neighbours(image, i, j, outside)
                index = int(result, 2)
                temp.append(enhance[index])
            new_image.append(temp)
        image = new_image
        outside = enhance[0] if outside == '.' else enhance[-1]

    total_lit = 0
    for row in image:
        total_lit += sum(x == '#' for x in row)
    return total_lit


def solve_task1():
    return solve(2)


def solve_task2():
    return solve(50)


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
