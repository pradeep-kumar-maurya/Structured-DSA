def find_second_smallest(arr):
    min = arr[0]
    diff = float('-inf')
    second_min_element_index = None

    if len(arr) == 1:
        return -1

    for num in arr:
        if num < min:
            min = num
    
    for i in range(len(arr)):

        if min - arr[i] > diff and arr[i] != min:
            diff = min - arr[i]
            second_min_element_index = i

    return arr[second_min_element_index]


arr = [1, 2, 4, 3, 2, 1]
arr = [4, 3, 2, 1, 5, 6, 7, 0, 0, 8]
arr = [-4, -3, -2, -1, 0, 1]
arr = [4, 3, 2, 1]
arr = [1, 2, 3, 4, 5]
arr = [1, 2, 4, 7, 7, 5]
arr = [1]
print(find_second_smallest(arr))
