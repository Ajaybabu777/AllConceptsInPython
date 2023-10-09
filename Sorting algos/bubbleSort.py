def bubbleSort(arr,l):
    for i in range(l):
        print("i : ", i)
        print("arr[i] : ",arr[i])
        for j in range(0, l-1-i):
            print("array : ", arr)
            print("j : ", j)
            print("arr[j] : ", arr[j])
            print("arr[j+1] : ", arr[j+1])
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


arr = [8, 3, 1, 6, 4, 7, 2, 5]
l = len(arr)
print("length : ", l)
print(bubbleSort(arr,l))