arr = [7, 12, 9, 11, 11, 3]
print(arr)
n = len(arr)
for i in range(1, n):
    j = i-1
    curr_value = arr[i]
    while j>=0 and curr_value < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = curr_value
print(arr)