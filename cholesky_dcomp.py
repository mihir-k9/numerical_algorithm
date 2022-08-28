import numpy as np


def cholesky(matrix_a, matrix_b):
    """
    Solves Ax = b using LU factorisation. Main steps are:
    1. Get diagonal entries (L) using a formula to form lower triangle matrix, then transpose this (L').
    2. Solve Ly = B as an intermediate step.
    3. Solve Ux = y to get the upper triangle matrix.

    :parameter:
    matrix_a: numpy array (n x n)
        The matrix to decompose into LU.

    matrix_b: numpy array (n x 1)
        Column vector of answer.

    :return:

    x_vector: numpy array (n x 1)
        Column vector which solves Ax = b.

    """

    # Cholesky decomposition
    n = len(matrix_a)
    x_vector = np.ones((n, 1))
    matrix_l = np.zeros((n, n))
    matrix_l[0, 0] = np.sqrt(matrix_a[0, 0])

    for k in range(1, n):
        matrix_l[k, 0] = matrix_a[k, 0] / matrix_l[0, 0]

    # Get diagonal entries
    for j in range(1, n):
        matrix_l[j, j] = np.sqrt(matrix_a[j, j] - sum((matrix_l[j, s] ** 2) for s in range(j)))
        if j > 0:
            for p in range(j + 1, n):
                matrix_l[p, j] = (matrix_a[p, j] - sum(matrix_l[j, t] * matrix_l[p, t] for t in range(j))) / matrix_l[
                    j, j]

    # Transpose matrix
    l_transpose = np.array([[matrix_l[j][i] for j in range(len(matrix_l))] for i in range(len(matrix_l[0]))])

    y_vector_f = np.ones((n, 1))
    y_vector_f[0, 0] = matrix_b[0, 0] / matrix_l[0, 0]

    # Solve Ly = B
    for d in range(1, n):
        y_vector_f[d, 0] = (matrix_b[d, 0] - sum(matrix_l[d, k] * y_vector_f[k, 0] for k in range(d))) / \
                           l_transpose[d, d]

    x_vector[n - 1, 0] = y_vector_f[n - 1, 0] / l_transpose[n - 1, n - 1]

    # Solve Ux = y
    for v in range(n - 2, -1, -1):
        x_vector[v, 0] = (y_vector_f[v, 0] - sum(l_transpose[v, k] * x_vector[k, 0] for k in range(v + 1, n))) / \
                           l_transpose[v, v]

    return x_vector

