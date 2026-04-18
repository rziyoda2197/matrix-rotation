import pytest
import numpy as np

def rotate_matrix(matrix):
    return np.rot90(matrix, -1)

@pytest.mark.parametrize("matrix, expected", [
    (np.array([[1, 2], [3, 4]]), np.array([[3, 1], [4, 2]])),
    (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), np.array([[7, 4, 1], [8, 5, 2], [9, 6, 3]])),
    (np.array([[1]]), np.array([[1]])),
])
def test_rotate_matrix(matrix, expected):
    assert np.array_equal(rotate_matrix(matrix), expected)
