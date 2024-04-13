def BubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = BubbleSort(arr)
print("Here is the sorted list:")
print(sorted_arr)
