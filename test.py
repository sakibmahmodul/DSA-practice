# # Bubble Sort
# arr = [7, 12, 9, 11, 3]
# n = len(arr)
# print(arr)
# for i in range(n-1):
#     swap = False
#     for j in range(n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             swap = True
#     if not swap:
#         break

# print(arr)

# Selection Sort
# arr = [7, 12, 9, 11, 3]
# n = len(arr)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1, n):
#         if arr[j]<arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)

# # Insertion Sort
# arr = [7, 12, 9, 11, 3]
# n = len(arr)
# for i in range(n-1):
#     j = i+1
#     while j>0:
#         if arr[j]<arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#             j -= 1
# print(arr)

# Quick Sort
arr = [37, 12, 9, 11 ]
def quickSort(arr, low, high):
    if low<high:
        pivot_pos = partition(arr, low, high)
        quickSort(arr, low, pivot_pos-1)
        quickSort(arr, pivot_pos+1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while i<=j:
        while i<=high and arr[i]<=pivot:
            i += 1
        while j>=low and arr[j]>pivot:
            j -= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

print(quickSort(arr, 0, len(arr) - 1))