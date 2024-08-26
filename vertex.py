class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, vertex):
        return self.x == vertex.x and self.y == vertex.y