import random
from vertex import Vertex
from triangulate import triangulate
import matplotlib.pyplot as plt


def plot_triangles(triangles):
    """
    Plots the given list of triangles.

    :param triangles: List of Triangle objects to plot.
    """
    plt.figure()
    for triangle in triangles:
        x = [triangle.v0.x, triangle.v1.x, triangle.v2.x, triangle.v0.x]
        y = [triangle.v0.y, triangle.v1.y, triangle.v2.y, triangle.v0.y]
        plt.plot(x, y, 'b-')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def main(num_points):
    """
    Main function to generate random points, triangulate them, and plot the resulting mesh.

    :param num_points: Number of random points to generate.
    """
    # Generate random points
    vertices = [Vertex(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_points)]

    # Perform triangulation
    triangles = triangulate(vertices)

    # Plot the triangulated mesh
    plot_triangles(triangles)


# Run the main function
if __name__ == "__main__":
    main(500)
