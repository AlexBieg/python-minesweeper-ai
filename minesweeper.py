"""This plays a game of minesweeper in the console."""


from box import Box
from random import randint


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
        start_game(int(height), int(width), int(bombs))
    else:
        print("Not starting game.")


def start_game(height, width, bombs):
    """Start the game."""
    isPlaying = True
    board = [[0 for x in range(width)] for y in range(height)]
    setup_board(board, height, width, bombs)
    print_board(board, height, width)
    while (isPlaying):
        print("Choose a box to click.")
        x = input("X Coordinate? ")
        y = input("Y Coordinate? ")
        selected = board[int(y)][int(x)]
        selected.click()
        if selected.isMine:
            print("You Lose!")
            isPlaying = False
        print_board(board, height, width)


def setup_board(board, height, width, bombs):
    """Set up a random board."""
    for col in range(0, width):
        for row in range(0, height):
            board[row][col] = Box()
    for bomb in range(0, bombs):
        placedBomb = False
        while not placedBomb:
            x = randint(0, width - 1)
            y = randint(0, height - 1)
            if not board[y][x].isMine:
                board[y][x].isMine = True
                placedBomb = True


def print_board(board, height, width):
    """Print board."""
    spaces = "           "

    print(spaces[:height//10+2], end=" ")
    for header in range(0, width):
        print(header, end=spaces[:width//10 - header//10 + 1])
    print()
    print(spaces[:height//10+2], end=" ")
    for bar in range(0, width):
        print("-", end=spaces[:width//10 + 1])
    print()

    for row in range(0, height):
        print(str(row) + "|", end=spaces[:height//10 - row//10 + 1])
        for col in range(0, width):
            print(board[row][col], end=spaces[:width//10 + 1])
        print()

"""Call main function"""
if __name__ == "__main__":
    main()
