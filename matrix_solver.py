
import numpy as np


def smaller_matrix(raw_matrix, column):
    """ Helper function to get a smaller matrix. """

    for i in range(len(raw_matrix)):
        new_matrix = np.delete(raw_matrix, i, 0)
        new_matrix = np.delete(new_matrix, column, 1)

        return new_matrix


def determinant(matrix):
    """ Function to calculate the determinant of any matrix. Uses helper function smaller_matrix() defined above.

    :parameter:
    matrix: numpy array float

    :return:
    answer: float
        Numerical value of the determinant.

    """

    (r, c) = matrix.shape

    if r == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    else:
        answer = 0
        for j in range(r):
            dummy = (-1) ** (0 + j) * matrix[0][j] * determinant(smaller_matrix(matrix, j))
            answer += dummy

        return answer


def tri_d_solve(a, b, c, d):

    """
    Tri-diagonal sparse matrix solver. All parameters have dimensions (n x 1).

    :parameter:
    a: array float
        Value along the first (lower) diagonal.
    b: array float
        Value along the middle diagonal.
    c: array float
        Value along the last (upper) diagonal.
    d: array float

    :return:
    x: flaat array
        Solution to Ax = d

    """
    n = len(b)
    x = np.zeros(n)

    for k in range(1, n):
        # First a is not used
        q = a[k] / b[k - 1]
        b[k] = b[k] - c[k - 1] * q
        d[k] = d[k] - d[k - 1] * q

    # Solve for last x
    q = d[-1] / b[-1]
    x[-1] = q

    for k in range(n - 2, -1, -1):
        # Last c is not used
        q = (d[k] - c[k] * q) / b[k]
        x[k] = q

    return x
