import numpy as np

# Vertices of the cube
VERTICES = np.array([
    [-0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5],
    [-0.5, 0.5, -0.5],
    [-0.5, 0.5, 0.5],
    [0.5, -0.5, -0.5],
    [0.5, -0.5, 0.5],
    [0.5, 0.5, -0.5],
    [0.5, 0.5, 0.5]
])



if __name__ == "__main__":
    _a_matrix = np.matrix(
        '1 2; \
         3 4'
    )
    _inverse_mat = np.linalg.inv(_a_matrix)
    print(_inverse_mat)
    print(_a_matrix*_inverse_mat)
    print(_inverse_mat*_a_matrix)
    print(_a_matrix+_inverse_mat)  # doesn't mean anything