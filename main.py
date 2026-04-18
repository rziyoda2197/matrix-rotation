import numpy as np

def matrix_rotation(matrix):
    return np.rot90(matrix, 1)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Asl matrix:")
print(matrix)

rotated_matrix = matrix_rotation(matrix)
print("\n90 daraja burilgan matrix:")
print(rotated_matrix)
```

```python
import numpy as np

def matrix_rotation(matrix):
    return np.rot90(matrix, 1)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Asl matrix:")
print(matrix)

rotated_matrix = matrix_rotation(matrix)
print("\n90 daraja burilgan matrix:")
print(rotated_matrix)
