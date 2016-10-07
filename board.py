"""A board for a minesweeper game."""


from box import Box
from random import randint


class Board(object):
    """Is a board."""

    def __init__(self, height, width, bombs):
        """Set up the board."""
        self.board = [[0 for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height
        self.bombs = bombs

        self.setup_board()

    def setup_board(self):
        """Set up a random board."""
        for col in range(0, self.width):
            for row in range(0, self.height):
                self.board[row][col] = Box(col, row)
        for bomb in range(0, self.bombs):
            placedBomb = False
            while not placedBomb:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
                if not self.board[y][x].isMine:
                    self.board[y][x].isMine = True
                    placedBomb = True
        for col in range(0, self.width):
            for row in range(0, self.height):
                if not self.board[row][col].isMine:
                    numMines = 0
                    cols = [col]
                    rows = [row]

                    if col-1 >= 0:
                        cols.append(col-1)
                    if col+1 < self.width:
                        cols.append(col+1)

                    if row-1 >= 0:
                        rows.append(row-1)
                    if row+1 < self.height:
                        rows.append(row+1)
                    for x in cols:
                        for y in rows:
                            if self.board[y][x].isMine:
                                numMines = numMines + 1
                    self.board[row][col].num = numMines

    def click_box(self, x, y):
        """Click selected box and clicks other empty connected ones."""
        box = self.board[y][x]
        box.click()
        if box.num < 1:
            cols = [box.x]
            rows = [box.y]

            if box.x-1 >= 0:
                cols.append(box.x-1)
            if box.x+1 < self.width:
                cols.append(box.x+1)

            if box.y-1 >= 0:
                rows.append(box.y-1)
            if box.y+1 < self.height:
                rows.append(box.y+1)

            for col in cols:
                for row in rows:
                    if not self.board[row][col].isClicked:
                        self.click_box(col, row)

    def click_all(self):
        """Click all boxes."""
        for col in range(0, self.width):
            for row in range(0, self.height):
                self.board[row][col].click()

    def check_win(self):
        """Check Win."""
        win = True
        for col in range(0, self.width):
            for row in range(0, self.height):
                if (not self.board[row][col].isMine
                   and not self.board[row][col].isClicked):
                    win = False
        return win

    def check_mine(self, x, y):
        """Check mine."""
        return self.board[y][x].isMine

    def print_board(self):
        """Print board."""
        spaces = "           "

        print(spaces[:self.height//10+2], end=" ")
        for header in range(0, self.width):
            print(header, end=spaces[:self.width//10 - header//10 + 1])
        print()
        print(spaces[:self.height//10+2], end=" ")
        for bar in range(0, self.width):
            print("-", end=spaces[:self.width//10 + 1])
        print()

        for row in range(0, self.height):
            print(str(row) + "|", end=spaces[:self.height//10 - row//10 + 1])
            for col in range(0, self.width):
                print(self.board[row][col], end=spaces[:self.width//10 + 1])
            print()
