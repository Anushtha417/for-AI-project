import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

wins = 0
losses = 0
draws = 0

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    for row in board:
        if EMPTY in row:
            return None

    return 'Draw'

def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == AI:
        return 1
    if result == HUMAN:
        return -1
    if result == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = AI

def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == EMPTY:
                board[row][col] = HUMAN
                break
            else:
                print("Cell already occupied.")
        except:
            print("Invalid input. Try again.")

def play_game():
    global wins, losses, draws
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    print_board(board)

    while True:
        human_move(board)
        print_board(board)
        result = check_winner(board)
        if result:
            break

        ai_move(board)
        print("AI played:")
        print_board(board)
        result = check_winner(board)
        if result:
            break

    if result == HUMAN:
        print("You win!")
        wins += 1
    elif result == AI:
        print("AI wins!")
        losses += 1
    else:
        print("It's a draw!")
        draws += 1

def main():
    while True:
        play_game()
        print("\nScoreboard")
        print("Wins:", wins, "Losses:", losses, "Draws:", draws)

        choice = input("\nPlay again? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()


