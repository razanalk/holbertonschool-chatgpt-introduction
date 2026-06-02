def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while not check_winner(board):
        print_board(board)

        try:
            row = int(input(
                "Enter row (0, 1, or 2) for player " + player + ": "
            ))
            col = int(input(
                "Enter column (0, 1, or 2) for player " + player + ": "
            ))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Try again.")
            continue

        if board[row][col] == " ":
            board[row][col] = player

            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)

    winner = "O" if player == "X" else "X"
    print("Player " + winner + " wins!")
