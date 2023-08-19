n = eval(input("enter number: "))

nums = [None]*(n+1)
nums[0]=nums[1] = 1
for i in range(2,n+1):
    nums[i] = nums[i-1]+nums[i-2]
print(nums[n])