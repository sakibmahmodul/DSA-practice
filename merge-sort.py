def mergeSort(arr, start, end):
    if start >= end:
        return [arr[start]] if start == end else []
    mid = (start + end) // 2
    left = mergeSort(arr, start, mid)
    right = mergeSort(arr, mid + 1, end)
    return merge(left, right)

def merge(left, right):
    new = []
    i, j = 0, 0
    # Merge elements from both halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    # Append remaining elements from `left` and `right`
    new.extend(left[i:])
    new.extend(right[j:])
    return new

# Example usage
arr = [7, 12, 9, 11, 11, 3]
print(mergeSort(arr, 0, len(arr) - 1))