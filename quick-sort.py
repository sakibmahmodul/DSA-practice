arr = [7, 12, 9, 11, 11, 3]

def quickSort(arr, start, end):
    if start < end:
        pivot_pos = partition(arr, start, end)
        # Correct recursive calls
        quickSort(arr, start, pivot_pos - 1)
        quickSort(arr, pivot_pos + 1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end
    while i <= j:
        # Move `i` to the right until an element greater than the pivot is found
        while i <= end and arr[i] <= pivot:
            i += 1
        # Move `j` to the left until an element smaller than or equal to the pivot is found
        while j >= start and arr[j] > pivot:
            j -= 1
        # Swap elements if `i` is still less than `j`
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot in its correct position
    arr[start], arr[j] = arr[j], arr[start]
    return j

print(quickSort(arr, 0, len(arr) - 1))