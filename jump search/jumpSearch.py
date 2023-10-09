import math

def jumpSearch(a,l,t):
    print("a : ",a)
    print("l : ", l)
    step = int(math.sqrt(l))
    print("step : ",step)
    prev = 0
    print("Prev : ",prev)

    index = min(step,l)-1
    print(a[index])
    while a[min(step,l)-1] <  t:
        print(a[index])
        prev = step
        print("Prev : ",prev)
        step = step + int(math.sqrt(l))
        print("step : ",step)
        if prev >=l:
            return ("not found")
        
    for position in range(prev, min(step,l)):
        if a[position] == t:
            return position

    return("not found") 


arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
l = len(arr)
t = 7
print(jumpSearch(arr,l,t))