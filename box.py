"""A box in a minesweeper game that could contain a mine."""


class Box(object):
    """is a box."""

    def __init__(self, isMine=False, isFlagged=False, isClicked=False, num=0):
        """Initialize the box."""
        self.isMine = isMine
        self.isFlagged = isFlagged
        self.isClicked = isClicked
        self.num = num

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
