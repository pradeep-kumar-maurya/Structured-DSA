def find_missing(arr):

    n = len(arr) + 1
    actual_sum = n * (n + 1) // 2
    sum = 0

    for num in arr:
        sum += num

    return actual_sum - sum


print(find_missing([1, 2, 4, 5]))
print(find_missing([1, 3]))
