def count_subarray(arr, k):
    '''
    This approach does not work because we should not be building the prefix_dict ahead. prefix_dict must be built one by one
    and not at one go.
    '''
    prefix_arr = [0] * len(arr)
    prefix_arr[0] = arr[0]
    freq_dict = {arr[0]: 1}
    count = 0

    for i in range(1, len(arr)):

        prefix_arr[i] = prefix_arr[i - 1] + arr[i]

        if freq_dict.get(prefix_arr[i]) is None:
            freq_dict[prefix_arr[i]] = 1
        else:
            freq_dict[prefix_arr[i]] += 1

    for i in range(len(prefix_arr)):

        if prefix_arr[i] == k:
            count += 1

        if freq_dict.get(prefix_arr[i] - k) is not None:
            count += freq_dict.get(prefix_arr[i] - k)

    return count


print(count_subarray([3, 1, 2, 4], 6))
print(count_subarray([1, 2, 3], 3))
print(count_subarray([1], 0))
print(count_subarray([-1, -1, 1], 0))
print(count_subarray([0, 0, 0, 3], 3))
print(count_subarray([0, 0, 3, 0, 3, 0], 3))
