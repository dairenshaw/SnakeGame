import random
from config import COLOURS, CONFIG

class Food():
    def __init__(self):
        self.X = round(random.randint(0, CONFIG["X"] - CONFIG["SIZE"]), -1)
        self.Y = round(random.randint(0, CONFIG["Y"] - CONFIG["SIZE"]), -1)
        self.Colour = COLOURS["LightBlue"]