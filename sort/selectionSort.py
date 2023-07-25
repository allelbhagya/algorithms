"""
time complexity - O(n^2)
"""

def selectionSort(data):
    for step in range(len(data)):
        min_index = step
        for i in range(step+1, len(data)):
            if data[i]<data[min_index]:
                min_index = i
        (data[step], data[min_index]) = (data[min_index], data[step])
    return data

values = [1,2,7,-10, 11, 23, 0]

print(selectionSort(values))