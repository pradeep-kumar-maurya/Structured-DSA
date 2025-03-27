def remove_duplicates(arr):
    index = 0

    for i in range(len(arr)):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]
    
    return arr[: index + 1]


def union(arr1, arr2):
    
    i = 0
    j = 0
    sorted_array = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1

    return remove_duplicates(sorted_array)


print(union([1, 2, 3, 4, 5], [2, 3, 4, 4, 5]))
print(union([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 4, 5, 11, 12]))
