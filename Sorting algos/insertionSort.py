def insertionSort(arr,l):
    for i in range(1,l):
        j = i-1
        temp = arr[i]
        while j>=0 and temp<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
    return arr
        
arr = [8, 3, 1, 6,11]
l = len(arr)
print(insertionSort(arr,l))