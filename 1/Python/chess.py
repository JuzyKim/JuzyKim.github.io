
chessboard = [[0 for _ in range(8)] for _ in range(8)]

moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def is_valid_move(x, y):
    return 0 <= x < 8 and 0 <= y < 8 and chessboard[x][y] == 0

def find_possible_moves(x, y):
    possible_moves = []
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y):
            possible_moves.append((new_x, new_y))
    return possible_moves

def explore_moves(x, y, move_number):
    if move_number > 8 * 8:
        return True
    chessboard[x][y] = move_number
    possible_moves = find_possible_moves(x, y)
    for new_x, new_y in possible_moves:
        if explore_moves(new_x, new_y, move_number + 1):
            return True
    chessboard[x][y] = 0
    return False

start_x, start_y = 0, 0
if explore_moves(start_x, start_y, 1):
    
    for row in chessboard:
        print(row)
else:
    print("No solution found.")