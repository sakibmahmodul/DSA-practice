arr = [3, 5, 2, 6, 4, 3, 5, 4, 3, 2]
def countingSort(arr):
    n = len(arr)
    if n<=1:
        return arr
    max_value = max(arr)
    min_value = min(arr)
    range_value = max_value - min_value + 1
    count = [0] * range_value
    for item in arr:
        count[item - min_value] += 1
    index = 0
    for i in range(range_value):
        while count[i]>0:
            arr[index] = i + min_value
            index += 1
            count[i] -= 1
    return arr
print(countingSort(arr))

