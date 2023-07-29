"""
time complexity = O(log n)
"""

def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (high+low)//2
        if arr[mid]<target:
            low = mid + 1
        elif arr[mid]>target:
            high = mid - 1
        else:
            return mid
    return False

arr = [1,3,6,7,10,15,62,100]
target = 15
res = binary_search(arr,target)
if res:
    print("Target found at", res)
else:
    print("Target not found")