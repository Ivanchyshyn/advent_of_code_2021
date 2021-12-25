import json
import math
from itertools import permutations

from node import TreeNode


def parse_input():
    with open('day18/input.txt') as fp:
        return fp.read().strip().split('\n')


def parse_line(line):
    depth = 0
    head = current = None
    before = ''
    for char in line:
        if char == '[':
            before += char
            depth += 1
        elif char == ']':
            before += char
            depth -= 1
        elif char == ',':
            before += char
            continue
        elif head is None:
            head = current = TreeNode(int(char), depth, before=before)
            before = ''
        else:
            node = TreeNode(int(char), depth, left=current, before=before)
            current.right = node
            current = node
            before = ''
    return head


def explode_pair(cur):
    next_node = cur.right
    if cur.left:
        cur.left.value += cur.value
    if next_node.right:
        next_node.right.value += next_node.value
        next_node.right.left = cur
        next_node.right.before = next_node.right.before[1:]

    cur.value = 0
    cur.depth -= 1
    cur.before = cur.before[:-1]
    cur.right = next_node.right


def split_number(cur):
    div = cur.value / 2
    left, right = math.floor(div), math.ceil(div)
    next_node = cur.right

    cur.value = left
    cur.depth += 1
    cur.before += '['

    new_node = TreeNode(
        right, cur.depth, left=cur, right=next_node, before=','
    )

    cur.right = new_node
    if next_node:
        next_node.before = ']' + next_node.before
        next_node.left = new_node


def check_explode(cur):
    return cur.depth >= 5


def check_split(cur):
    return cur.value >= 10


def find_magnitude(pairs):
    if not isinstance(pairs, list):
        return pairs
    return 3 * find_magnitude(pairs[0]) + 2 * find_magnitude(pairs[1])


def solve(head, line):
    head2 = parse_line(line)
    head += head2
    can_check_split = False
    while True:
        cur = head
        while cur:
            if check_explode(cur):
                explode_pair(cur)
                break
            if can_check_split and check_split(cur):
                split_number(cur)
                can_check_split = False
                break

            cur = cur.right
        else:
            if can_check_split:
                break
            can_check_split = True


def solve_task1():
    lines = parse_input()
    it = iter(lines)
    head = parse_line(next(it))

    for line in it:
        solve(head, line)

    return find_magnitude(json.loads(head.to_string()))


def solve_task2():
    lines = parse_input()
    max_magnitude = 0
    for line1, line2 in permutations(lines, 2):
        head = parse_line(line1)
        solve(head, line2)
        magnitude = find_magnitude(json.loads(head.to_string()))
        max_magnitude = max(max_magnitude, magnitude)
    return max_magnitude


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
