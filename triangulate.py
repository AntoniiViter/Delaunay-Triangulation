from triangle import Triangle, get_super_triangle
from edge import Edge


def unique_edges(edges):
    uniq_edges = []

    for i in range(len(edges)):
        is_unique = True

        # Check if edge is unique
        for j in range(len(edges)):
            if i != j and edges[i].equals(edges[j]):
                is_unique = False
                break

        if is_unique:
            uniq_edges.append(edges[i])

    return uniq_edges


def add_vertex(vertex, triangles):
    edges = []

    def filter_and_collect_edges(triangle):
        if triangle.in_circum_cycle(vertex):
            edges.extend([
                Edge(triangle.v0, triangle.v1),
                Edge(triangle.v1, triangle.v2),
                Edge(triangle.v2, triangle.v0)
            ])
            return False  # Exclude this triangle
        return True  # Include this triangle

    triangles = list(filter(filter_and_collect_edges, triangles))

    edges = unique_edges(edges)

    for edge in edges:
        triangles.append(Triangle(edge.v0, edge.v1, vertex))

    return triangles


def triangulate(vertices):
    super_triangle = get_super_triangle(vertices)

    triangles = [super_triangle]

    for vertex in vertices:
        triangles = add_vertex(vertex, triangles)

    triangles = [triangle for triangle in triangles if not (
            triangle.v0 == super_triangle.v0 or triangle.v0 == super_triangle.v1 or triangle.v0 == super_triangle.v2 or
            triangle.v1 == super_triangle.v0 or triangle.v1 == super_triangle.v1 or triangle.v1 == super_triangle.v2 or
            triangle.v2 == super_triangle.v0 or triangle.v2 == super_triangle.v1 or triangle.v2 == super_triangle.v2
    )]

    return triangles

