import heapq
from collections import defaultdict


def parse_input():
    with open('day15/input.txt') as fp:
        return [
            list(map(int, value))
            for value in fp.read().strip().split('\n')
        ]


def get_neighbours(matrix, node):
    i, j = node
    rows, cols = len(matrix), len(matrix[0])
    for x, y in (
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ):
        if 0 <= x < rows and 0 <= y < cols:
            yield (x, y), matrix[x][y]


def dijkstra(matrix, starting_node, finish_node):
    """The algorithm:
    https://levelup.gitconnected.com/dijkstra-algorithm-in-python-8f0e75e3f16e
    1. Create a set "seen" to keep track of visited nodes.
    2. Create a dictionary "nodeCosts" for keeping track of minimum costs for
    reaching different nodes from the source node,
    and initialize the cost for the source node as 0.
    3. Create a priority queue data structure and
    push a tuple (0, source node) in the Priority Queue (heap), representing
    (the cost to the node from the source node, the node itself).
    4. Loop inside a while loop until there is nothing in the priority queue.
    While looping, pop the node with minimum cost.
    5. Loop through all of the node's adjacent nodes.
    if they have not been explored before, and have total costs minimum than
    the cost in the "nodeCosts" add them too to the priority queue.
    """
    visited = set()
    pq = []
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[starting_node] = 0
    heapq.heappush(pq, (0, starting_node))

    while pq:
        # go greedily by always extending the shorter cost nodes first
        cost, node = heapq.heappop(pq)
        if node == finish_node:
            break
        if node in visited:
            continue
        visited.add(node)

        for adj_node, weight in get_neighbours(matrix, node):
            if adj_node in visited:
                continue

            new_cost = cost + weight
            if node_costs[adj_node] > new_cost:
                node_costs[adj_node] = new_cost
                heapq.heappush(pq, (new_cost, adj_node))

    return node_costs[finish_node]


def get_value(num):
    if num == 9:
        return 1
    return num + 1


def multiply_matrix(matrix, times):
    # Multiply columns
    for row in matrix:
        prev_row = row[:]
        for _ in range(times - 1):
            temp = [get_value(num) for num in prev_row]
            prev_row = temp
            row.extend(temp)

    # Multiply rows
    rows = len(matrix)
    for i in range(rows * (times - 1)):
        row = matrix[i]
        matrix.append([get_value(num) for num in row])

    return matrix


def solve_task1():
    matrix = parse_input()
    rows, cols = len(matrix), len(matrix[0])
    return dijkstra(matrix, (0, 0), (rows - 1, cols - 1))


def solve_task2():
    matrix = parse_input()
    matrix = multiply_matrix(matrix, 5)
    rows, cols = len(matrix), len(matrix[0])
    return dijkstra(matrix, (0, 0), (rows - 1, cols - 1))


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
