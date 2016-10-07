"""A box in a minesweeper game that could contain a mine."""


class Box(object):
    """is a box."""

    def __init__(self, x=0, y=0):
        """Initialize the box."""
        self.isMine = False
        self.isFlagged = False
        self.isClicked = False
        self.num = 0
        self.x = x
        self.y = y

    def __str__(self):
        """Return string of object."""
        if self.isClicked:
            if self.isMine:
                return "*"
            else:
                return str(self.num)
        else:
            if self.isFlagged:
                return "!"
            else:
                return "+"

    def click(self):
        """Click box."""
        self.isClicked = True
