arr= [2,3,4,5]#arr = [64, 34,25, 12, 22, 22, 11, 90, 5]
n = len(arr)
for i in range(n-1): # case 1: i=0
    swap = False #swap = False
    for j in range(n-i-1): # j=0; 1; 2
        if arr[j]>arr[j+1]: #64>34?; 64>25?; 64>12?;
            arr[j], arr[j+1] = arr[j+1], arr[j] #swap (64, 34) arr = [34, 64,25, 12, 22, 22, 11, 90, 5]; swap(64,25) arr = [34, 25 ,64, 12, 22, 22, 11, 90, 5]
            swap = True #swap = True; swap = True
    if not swap: 
        break
print(arr)