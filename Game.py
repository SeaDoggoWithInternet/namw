class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            
