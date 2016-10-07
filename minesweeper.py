"""This plays a game of minesweeper in the console."""


from board import Board


def main():
    """The main method that starts the game."""
    print("Welcome to Minesweeper!")
    start = input("Are you ready to start the game? ")
    if start.lower().startswith("y"):
        print("starting game!")
        height = input("What should the height be? (1-99)")
        width = input("What should the width be? (1-99)")
        bombs = input("How many bombs should there be? (1-" + str(int(width) *
                      int(height)) + ")")
        start_game(Board(int(height), int(width), int(bombs)))
    else:
        print("Not starting game.")


def start_game(board):
    """Start the game."""
    isPlaying = True
    board.print_board()
    while (isPlaying):
        print("Choose a box to click.")
        coords = input("Coordinates to click? (x y format. ex: 4 10) ").split()
        board.click_box(int(coords[0]), int(coords[1]))
        if board.check_mine(int(coords[0]), int(coords[1])):
            print("You Lose!")
            isPlaying = False
            board.click_all()
        else:
            if board.check_win():
                print("You Win!!")
                isPlaying = False
                board.click_all()
        board.print_board()


"""Call main function"""
if __name__ == "__main__":
    main()
