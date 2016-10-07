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
        coords = input("Coordinates to click? (x y format. ex: 4 10) ").split()
        selected = board[int(coords[1])][int(coords[0])]
        click_box(selected, board, width, height)
        if selected.isMine:
            print("You Lose!")
            isPlaying = False
            click_all(board, width, height)
        else:
            if check_win(board, width, height):
                print("You Win!!")
                isPlaying = False
                click_all(board, width, height)
        print_board(board, height, width)


def click_box(box, board, width, height):
    box.click()
    if box.num < 1:
        cols = [box.x]
        rows = [box.y]

        if box.x-1 >= 0:
            cols.append(box.x-1)
        if box.x+1 < width:
            cols.append(box.x+1)

        if box.y-1 >= 0:
            rows.append(box.y-1)
        if box.y+1 < height:
            rows.append(box.y+1)

        for x in cols:
            for y in rows:
                if not board[y][x].isClicked:
                    click_box(board[y][x], board, width, height)


def click_all(board, width, height):
    for col in range(0, width):
        for row in range(0, height):
            board[row][col].click()


def check_win(board, width, height):
    win = True
    for col in range(0, width):
        for row in range(0, height):
            if not board[row][col].isMine and not board[row][col].isClicked:
                win = False

    return win


def setup_board(board, height, width, bombs):
    """Set up a random board."""
    for col in range(0, width):
        for row in range(0, height):
            board[row][col] = Box(col, row)
    for bomb in range(0, bombs):
        placedBomb = False
        while not placedBomb:
            x = randint(0, width - 1)
            y = randint(0, height - 1)
            if not board[y][x].isMine:
                board[y][x].isMine = True
                placedBomb = True
    for col in range(0, width):
        for row in range(0, height):
            if not board[row][col].isMine:
                numMines = 0
                cols = [col]
                rows = [row]

                if col-1 >= 0:
                    cols.append(col-1)
                if col+1 < width:
                    cols.append(col+1)

                if row-1 >= 0:
                    rows.append(row-1)
                if row+1 < height:
                    rows.append(row+1)
                for x in cols:
                    for y in rows:
                        if board[y][x].isMine:
                            numMines = numMines + 1
                board[row][col].num = numMines


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
