import math
from vertex import Vertex


def line_from_points(p1, p2):
    """
    Calculate the line equation coefficients (a, b, c) from two points

    :param p1: Tuple representing the coordinates of the first point (x, y).
    :param p2: Tuple representing the coordinates of the second point (x, y).
    :return: Coefficients a, b, c of the line equation ax + by = c.
    """

    a = p2.y - p1.y
    b = p1.x - p2.x
    c = a * p1.x + b * p1.y
    return a, b, c


def perpendicular_bisector_from_line(p1, p2, a, b):
    """
    Convert the line formed by two points to its perpendicular bisector.

    :param p1: Tuple representing the coordinates of the first point (x, y).
    :param p2: Tuple representing the coordinates of the second point (x, y).
    :param a: Coefficient 'a' of the line equation.
    :param b: Coefficient 'b' of the line equation.
    :return: Coefficients a, b, c of the perpendicular bisector line equation.
    """
    mid_point = Vertex((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0)

    # Perpendicular bisector: c = -bx + ay
    c = -b * mid_point.x + a * mid_point.y
    return -b, a, c


def line_line_intersection(a1, b1, c1, a2, b2, c2):
    """
    Calculate the intersection point of two lines.

    :param a1, b1, c1: Coefficients of the first line equation.
    :param a2, b2, c2: Coefficients of the second line equation.
    :return: Coordinates of the intersection point (x, y).
    """
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        # Lines are parallel; no intersection
        return [float('inf'), float('inf')]
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return Vertex(x, y)


def find_circumcenter(v0, v1, v2):
    """
    Find the circumcenter of a triangle formed by three points.

    :param v0: Tuple representing the coordinates of the first vertex (x, y).
    :param v1: Tuple representing the coordinates of the second vertex (x, y).
    :param v2: Tuple representing the coordinates of the third vertex (x, y).
    :return: Coordinates of the circumcenter (x, y).
    """
    # Line v0v1 is represented as ax + by = c
    a, b, c = line_from_points(v0, v1)

    # Line v1v2 is represented as ex + fy = g
    e, f, g = line_from_points(v1, v2)

    # Convert lines v0v1 and v1v2 to perpendicular bisectors
    a, b, c = perpendicular_bisector_from_line(v0, v1, a, b)
    e, f, g = perpendicular_bisector_from_line(v1, v2, e, f)

    # The point of intersection of these bisectors is the circumcenter
    circumcenter = line_line_intersection(a, b, c, e, f, g)

    return circumcenter


def calculate_radius(center, vertex):
    """
    Calculate the radius of the circumcircle.

    :param center: Tuple representing the coordinates of the circumcenter (x, y).
    :param vertex: Tuple representing the coordinates of a vertex on the circumcircle (x, y).
    :return: Radius of the circumcircle.
    """
    return ((center.x - vertex.x) ** 2 + (center.y - vertex.y) ** 2) ** 0.5


def get_super_triangle(vertices):
    """
    Creates a large triangle that encompasses all given vertices.

    :param vertices: List of Vertex objects representing the vertices to encompass.
    :return: A Triangle object representing the super triangle.
    """
    minx = miny = float('inf')
    maxx = maxy = float('-inf')

    for vertex in vertices:
        minx = min(minx, vertex.x)
        miny = min(miny, vertex.y)
        maxx = max(maxx, vertex.x)
        maxy = max(maxy, vertex.y)

    dx = (maxx - minx) * 10
    dy = (maxy - miny) * 10

    v0 = Vertex(minx - dx, miny - dy * 3)
    v1 = Vertex(minx - dx, maxy + dy)
    v2 = Vertex(maxx + dx * 3, maxy + dy)

    return Triangle(v0, v1, v2)


class Triangle:
    def __init__(self, v0: Vertex, v1: Vertex, v2: Vertex):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

        self.circum_center = find_circumcenter(v0, v1, v2)
        self.circum_radius = calculate_radius(self.circum_center, v0)

    def in_circum_cycle(self, v):
        dx = self.circum_center.x - v.x
        dy = self.circum_center.y - v.y

        return math.sqrt(dx * dx + dy * dy) <= self.circum_radius
