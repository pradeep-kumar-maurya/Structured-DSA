def find_second_largest(arr):
    max = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > max:
            max = num

    for i in range(len(arr)):
        diff = arr[i] - num

        if diff > second_largest and arr[i] != max:
            second_largest = arr[i]

    return second_largest


arr = [1, 2, 4, 3, 2, 1]
arr = [4, 3, 2, 1]
arr = [-4, -3, -2, -1, 0, 1]
print(find_second_largest(arr))
