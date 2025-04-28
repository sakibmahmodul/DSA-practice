arr = [3, 5, 2, 6, 4, 3, 5, 4, 3, 2]
def counting_sort(arr):
    n = len(arr)
    max_val = max(arr) 
    count = [0] * (max_val+1)
    for i in range(n):
        count[arr[i]] += 1
    index = 0
    for i in range(max_val+1):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    return arr
print(counting_sort(arr))