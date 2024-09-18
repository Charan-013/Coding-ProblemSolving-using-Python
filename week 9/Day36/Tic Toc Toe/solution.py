def initializeBoard():
    board = []
    for i in range(3):
        l = [" "] * 3
        board.append(l)
    return board


board = initializeBoard()


def displayBoard(board):
    print("   0   1   2")
    print("  ___ ___ ___")
    for row_idx, row in enumerate(board):
        print(f"{row_idx}| {" | ".join(row)} |")
        if row_idx < 3:
            print(" |___|___|___|")


def takeTurn(board, player):
    while True:
        try:
            print(f"{player}'s Turn")
            row = int(input("enter row: "))
            col = int(input("enter col: "))
            if row in range(3) and col in range(3) and board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Invalid move, Try again")
        except ValueError:
            print("Please enter a valid number.")


def playGame():
    board = initializeBoard()
    player = "X"
    while not isGameOver(board):
        displayBoard(board)
        takeTurn(board, player)
        if player == "X":
            player = "O"
        else:
            player = "X"
    displayBoard(board)
    print("Game Over")
    if player == "O":
        return "Winner is X"
    else:
        return "Winner is O"


def isGameOver(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            # cleck rows
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            # cleck cols
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    for row in board:
        if " " in row:
            return False
    return False


def main():
    return


print(playGame())
