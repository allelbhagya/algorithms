def partition(array, low, high):

    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i+1

def quickSort(array, low, high):
    if low<high:
        part = partition(array,low,high)
        quickSort(array, low, part-1)
        quickSort(array, part+1, high)


data = [8,4,2,1,4,6,7,9]

quickSort(data, 0, len(data)-1)
print(data)