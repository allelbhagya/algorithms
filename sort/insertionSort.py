"""
time complexity - O(n^2)
"""

def insertionSort(data):
    for step in range(1, len(data)):
        key = data[step]
        j = step -1
        while j>= 0 and key < data[j]:
            data[j+1] = data[j]
            j = j-1
        data[j+1] = key
    return data
    
values = [1,2,7,-10, 11, 23, 0]

print(insertionSort(values))