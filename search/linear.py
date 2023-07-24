"""
time complexity = O(n)
"""

lis = [2,3,6,1,3,56,1,0,100,9]
flag = False
target = 0
for i in range(len(lis)):
    if lis[i] == target:
        flag = True
        print("target", target, "is found at", i+1)
if not flag:
    print("target", target, "is not found")