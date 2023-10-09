'''
Find the Missing Number
'''

shouldBeSum = 45
a = [1,2,3,4,5,6,7,8]
totalSum = sum(a)
if totalSum< shouldBeSum:
    missingNum = a[-1] + 1
    print(missingNum)
else:
    print("num not possible")
