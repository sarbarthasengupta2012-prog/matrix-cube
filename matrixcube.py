import math
import tkinter as tk

class Cube:
    def __init__(self):
        # Increased size to 100 so it's visible on screen
        self.vector = [
            [-100, -100, 100], [100, -100, 100], [100, 100, 100], [-100, 100, 100],
            [-100, -100, -100], [100, -100, -100], [100, 100, -100], [-100, 100, -100]
        ]
        self.connections = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

    def rotate(self, theta_x, theta_y, theta_z):
        rad_x, rad_y, rad_z = math.radians(theta_x), math.radians(theta_y), math.radians(theta_z)
        cos_x, cos_y, cos_z = math.cos(rad_x), math.cos(rad_y), math.cos(rad_z)
        sin_x, sin_y, sin_z = math.sin(rad_x), math.sin(rad_y), math.sin(rad_z)

        # Rotation Matrix for X
        rx = [[1, 0, 0], [0, cos_x, -sin_x], [0, sin_x, cos_x]]
        # Rotation Matrix for Y
        ry = [[cos_y, 0, sin_y], [0, 1, 0], [-sin_y, 0, cos_y]]
        # Rotation Matrix for Z
        rz = [[cos_z, -sin_z, 0], [sin_z, cos_z, 0], [0, 0, 1]]

        new_vectors = []
        for v in self.vector:
            point_matrix = [v]
            t = multiply(point_matrix, rx)
            t = multiply(t, ry)
            t = multiply(t, rz)
            new_vectors.append(t[0])

        self.vector = new_vectors


def multiply(matrix_a, matrix_b):
    # 1. Get the dimensions
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    if cols_a != rows_b:
        return "Error: Columns of A must match Rows of B!"
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

root = tk.Tk()
root.title("adminDatabase")
canvas = tk.Canvas(root, width=1000, height=400, bg="black")
canvas.pack()

txtLabel = tk.Label(root,text="Hack all I.P Adresses?",font=("Verdana",30))
txtLabel.pack()

root.mainloop()