"""
time complexity - O(n^2)
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i -1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

values = [1,2,7,-10, 11, 23, 0]

print(bubbleSort(values))