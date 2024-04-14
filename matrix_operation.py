import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

matrix = np.reshape(arr, (4, 3))
print(matrix)

print("\nAccess elements")
print(arr[1])
print(arr[2][0])

arr = np.append(arr, [[13,14,15,16]], 0)
print("\nElement Added")
print(arr)

arr = np.delete(arr,[1], 0)
print("\nElement Deleted")
print(arr)