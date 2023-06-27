import random

# Tic-Tac-Toe

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("-------------------")
    for i in range(0, 9, 3):
        print("|", board[i], "|", board[i+1], "|", board[i+2], "|")
        print("-------------------")

# Function to check if a player has won
def check_win(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Function for the computer's move
def computer_move():
    # Generate a random move
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)

    # Update the board
    board[move] = "O"

# Function to play the game
def play_game():
    print("\nCome on, let's play a game of Tic-Tac-Toe!\n")
    player_name = input("Please enter your name: ")
    current_player = "X"
    game_over = False

    while not game_over:
        print_board()

        if current_player == "X":
            # Player's move
            valid_move = False
            while not valid_move:
                move = input(player_name + ", enter your move (1-9): ")

                if move.isdigit():
                    move = int(move) - 1
                    if move >= 0 and move < 9 and board[move] == " ":
                        valid_move = True
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Invalid input. Try again.")

            # Update the board
            board[move] = current_player
        else:
            # Computer's move
            print("Computer's turn (O)")
            computer_move()

        # Check if the current player has won
        if check_win(current_player):
            print_board()
            if current_player == "X":
                print(player_name + " wins!")
            else:
                print("Computer wins!")
            game_over = True
        elif " " not in board:
            # Check if it's a tie
            print_board()
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
