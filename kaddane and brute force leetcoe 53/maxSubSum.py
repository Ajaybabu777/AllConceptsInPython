def kaddaneAlgo(nums):
    maxSum = nums[0]
    currentSum = nums[0]

    for i in range(1, len(nums)):
        print(nums[i])
        print(currentSum+nums[i])
        currentSum = max(nums[i], currentSum+nums[i])
        print(currentSum)  
        maxSum = max(maxSum, currentSum)
        print(maxSum)
    print(maxSum)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
kaddaneAlgo(nums)