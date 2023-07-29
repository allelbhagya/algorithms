"""
finding a contigous subarray(atleast 1 value) which has the largest sum

with brute force - O(n^3)
for (i=0,,,, n-1):
    for (j=i,,,,n-1):
        for(k = i,,,j):
            compute sum


optimization O(n^2)

for(i=0,,,n-1):
    for(j=i,,,,n-1):
        currentSum + num[j]

kadane

- keeping track of a maximum value through list
- sliding window?

"""

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSub = nums[0]
currentSum = 0
for i in nums:
    if currentSum < 0:
        currentSum = 0
    currentSum += i
    maxSub = max(currentSum, maxSub)
print(maxSub)