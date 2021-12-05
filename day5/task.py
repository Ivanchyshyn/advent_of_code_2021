from collections import defaultdict, Counter


def solve_task1():
    points_x = defaultdict(Counter)
    points_y = defaultdict(Counter)
    with open('day5/input.txt') as fp:
        for line in fp:
            first, second = line.split('->', 1)
            x1, y1 = first.strip().split(',')
            x2, y2 = second.strip().split(',')
            if x1 == x2:
                x1, y1, y2 = int(x1), int(y1), int(y2)
                points_x[x1].update(range(min(y1, y2), max(y1, y2) + 1))
            elif y1 == y2:
                x1, x2, y1 = int(x1), int(x2), int(y1)
                points_y[y1].update(range(min(x1, x2), max(x1, x2) + 1))
    total = set()
    for key, counter in points_x.items():
        for num, times in counter.items():
            if times >= 2:
                total.add((key, num))
            if num in points_y and key in points_y[num]:
                total.add((key, num))

    for key, counter in points_y.items():
        for num, times in counter.items():
            if times >= 2:
                total.add((num, key))
            if num in points_x and key in points_x[num]:
                total.add((num, key))
    return len(total)


def solve_task2():
    points = []
    max_x = max_y = 0
    with open('day5/input.txt') as fp:
        for line in fp:
            first, second = line.split('->', 1)
            x1, y1 = first.strip().split(',')
            x2, y2 = second.strip().split(',')
            x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)
            points.append([(x1, y1), (x2, y2)])
    res = [[0] * (max_y + 1) for _ in range(max_x + 1)]
    total = 0
    for (x1, y1), (x2, y2) in points:
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            while y1 != y2 + 1:
                res[y1][x1] += 1
                if res[y1][x1] == 2:
                    total += 1
                y1 += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            while x1 != x2 + 1:
                res[y1][x1] += 1
                if res[y1][x1] == 2:
                    total += 1
                x1 += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            while x1 != x2 + 1:
                res[y1][x1] += 1
                if res[y1][x1] == 2:
                    total += 1
                x1 += 1
                if y1 < y2:
                    y1 += 1
                else:
                    y1 -= 1
    return total


if __name__ == '__main__':
    result1 = solve_task1()
    result2 = solve_task2()
    print('task 1 -', result1)
    print('task 2 -', result2)
