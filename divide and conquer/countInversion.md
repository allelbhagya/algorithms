function mergeAndCount(arr, left, mid, right):

    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays to store left and right subarrays
    left_arr[1..n1]
    right_arr[1..n2]

    # Copy data to temporary arrays
    for i from 1 to n1:
        left_arr[i] = arr[left + i - 1]

    for j from 1 to n2:
        right_arr[j] = arr[mid + j]

    # Initialize indices for merging
    i = 1
    j = 1
    k = left
    inv_count = 0

    # Merge the temporary arrays back into arr
    while i <= n1 and j <= n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i + 1
        else:
            arr[k] = right_arr[j]
            j = j + 1
            inv_count = inv_count + (n1 - i + 1)  # Count inversions

        k = k + 1

    # Copy the remaining elements of left_arr and right_arr
    while i <= n1:
        arr[k] = left_arr[i]
        i = i + 1
        k = k + 1

    while j <= n2:
        arr[k] = right_arr[j]
        j = j + 1
        k = k + 1

    return inv_count

function countInversions(arr, left, right):
inv_count = 0

    if left < right:
        mid = (left + right) / 2

        # Recursively count inversions in left and right halves
        inv_count += countInversions(arr, left, mid)
        inv_count += countInversions(arr, mid + 1, right)

        # Merge the two halves and count inversions in the merge step
        inv_count += mergeAndCount(arr, left, mid, right)

    return inv_count
