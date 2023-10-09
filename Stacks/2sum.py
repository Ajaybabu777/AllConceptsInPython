def twoSum(a,t):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return([i,j])
                
            
arr = [8,9,1,3,4,5,6]
target = 17
callingTheFunc = twoSum(arr,target)
print(callingTheFunc)
# time complexity O(n^2)

# arr = [1,3,4,5,6,8,9]
# target = 9
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
# if n is length of array what wil be the time complexity 
# O(n), Big O notation



[1,3,4,5,6,8,9]

# 1+3     4+5
# 1+4     4+6
# 1+5     4+8
# 1+6     4+9
# 1+8
# 1+9     5+6
#         5+8
# 3+4     5+9
# 3+5    
# 3+6     6+8
# 3+8     6+9
# 3+9     8+9

        