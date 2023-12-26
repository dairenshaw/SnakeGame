from controls import DIRECTIONS
from config import COLOURS, CONFIG

class Snake():
    def __init__(self):
        self.X = CONFIG["X"] / 2
        self.Y = CONFIG["Y"] / 2
        self.Direction = DIRECTIONS.NONE
        self.Colour = COLOURS["Red"]
        self.Length = 0
        self.Tail = []
        self.RefreshRate = 15

    def Move(self):
        if self.Direction == DIRECTIONS.LEFT:
            self.X -= CONFIG["SIZE"]
        if self.Direction == DIRECTIONS.RIGHT:
            self.X += CONFIG["SIZE"]
        if self.Direction == DIRECTIONS.UP:
            self.Y -= CONFIG["SIZE"]
        if self.Direction == DIRECTIONS.DOWN:
            self.Y += CONFIG["SIZE"]