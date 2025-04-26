# # Bubble Sort
arr = [7, 12, 9, 11, 3]
n = len(arr)
print(arr)
for i in range(n-1):
    swap = False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True
    if not swap:
        break

print(arr)