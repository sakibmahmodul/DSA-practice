arr = [7, 12, 9, 11, 3]
n = len(arr) 
for i in range(n-1):
   min_index = i
   j = i+1
   while(j<n):
      if arr[j]<arr[min_index]:
         min_index = j
   arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)