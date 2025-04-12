arr = [7, 12, 9, 11, 3]
n = len(arr)
for i in range(n-1):
    j = n-1
    while j > 0:
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
print("Sorted array is:", arr)

# Time complexity: O(n^2)
# Space complexity: O(1)