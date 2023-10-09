def binarySearch(a,l,t):
    start = 0
    end = len(a)-1

    while end >= start:
        mid = (start+end)//2

        if t == a[mid]:
            return mid
        
        elif t > a[mid]:
            start = mid+1

        elif t < a[mid]:
            end = mid-1
            

        else:
            return("target not found")


arr = [7, 2, 10, 5, 3, 8, 1, 6, 9, 4]
sotedArr = sorted(arr)
l = len(arr)
target = 4
print(binarySearch(sotedArr,l,target))