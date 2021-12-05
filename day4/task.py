
MARK = "X"


def get_draws_and_boards():
    boards = []
    temp_board = []
    with open('day4/input.txt') as fp:
        draws = fp.readline().strip().split(',')
        fp.readline()
        for line in fp:
            line = line.strip()
            if not line:
                boards.append(temp_board)
                temp_board = []
            else:
                temp_board.append(line.split())
    if temp_board:
        boards.append(temp_board)
    return draws, boards


def get_winner(draws, boards):
    boards_won = set()
    for draw in draws:
        for board_index, board in enumerate(boards):
            if board_index in boards_won:
                continue

            for row in board:
                for i, num in enumerate(row):
                    if num == draw:
                        row[i] = MARK
                        if check_board(board, row, i):
                            yield board, draw
                            boards_won.add(board_index)


def check_board(board, cur_row, col):
    return (
        all(x == MARK for x in cur_row) or
        all(row[col] == MARK for row in board)
    )


def get_result(winner, draw):
    return sum(
        int(num) for row in winner
        for num in row if num != MARK
    ) * int(draw)


def solve_task1():
    draws, boards = get_draws_and_boards()
    winner, draw = next(get_winner(draws, boards))
    return get_result(winner, draw)


def solve_task2():
    draws, boards = get_draws_and_boards()
    winner = draw = None
    for winner, draw in get_winner(draws, boards):
        # exhaust generator
        pass
    return get_result(winner, draw)


if __name__ == '__main__':
    result1 = solve_task1()
    result2 = solve_task2()
    print('task 1 -', result1)
    print('task 2 -', result2)
