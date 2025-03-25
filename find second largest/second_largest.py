def find_second_largest(arr):
    max = float('-inf')
    second_max = float('-inf')
    second_max_index = None

    if len(arr) == 1:
        return -1

    for num in arr:
        if num > max:
            max = num

    for i in range(len(arr)):
        diff = arr[i] - num

        if (diff > second_max and arr[i] != max):
            second_max = diff
            second_max_index = i

    return arr[second_max_index]


arr = [1, 2, 4, 3, 2, 1]
arr = [4, 3, 2, 1, 5, 6, 7, 0, 0, 8]
arr = [-4, -3, -2, -1, 0, 1]
arr = [4, 3, 2, 1]
arr = [1, 2, 3, 4, 5]
arr = [1, 2, 4, 7, 7, 5]
arr = [1]
print(find_second_largest(arr))
