from vertex import Vertex


class Edge:
    def __init__(self, v0: Vertex, v1: Vertex):
        self.v0 = v0
        self.v1 = v1

    def equals(self, edge):
        return ((self.v0.equals(edge.v0) and self.v1.equals(edge.v1))
                or (self.v0.equals(edge.v1) and self.v1.equals(edge.v0)))
