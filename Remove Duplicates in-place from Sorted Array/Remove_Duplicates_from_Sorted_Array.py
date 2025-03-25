def remove_duplicates(arr):
    index = 0

    for i in range(1, len(arr)):
        
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]


    return index + 1



arr = [1, 1, 2, 2, 2, 3, 3]
arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
arr = [1, 2, 2, 2, 3]
arr = [1, 2, 3, 4, 5]
arr = [1, 1, 2, 3, 3, 4, 5, 5, 5]
print(remove_duplicates(arr))
