def max_sub_array(arr, k):

    max_size = 0
    prefix_array = [0] * len(arr)
    prefix_array[0] = arr[0]
    prefix_dict = {arr[0]: [0]}

    # The idea is to maintain a prefix sum array and a prefix sum dict with indexes as the values in the list format.
    for i in range(1, len(arr)):
        prefix_array[i] = prefix_array[i - 1] + arr[i]

        if prefix_dict.get(prefix_array[i]) is None:
            prefix_dict[prefix_array[i]] = [i]
        else:
            prefix_dict[prefix_array[i]].append(i)

    for num in prefix_array:

        # if num == k then max_size will be (last index of num + 1)
        if num == k:
            if prefix_dict[num][-1] > max_size:
                max_size = prefix_dict[num][-1] + 1
        
        # if num - k is present in the prefix_dict then max_size will be (last index of num - first index of (num - k))
        if prefix_dict.get(num - k) is not None:
            if (prefix_dict[num][-1] - prefix_dict[num - k][0]) > max_size:
                max_size = prefix_dict[num][-1] - prefix_dict[num - k][0]

    return max_size


print(max_sub_array([2, 3, 5], k = 5))
print(max_sub_array([2, 3, 5, 1, 9], k = 10))
print(max_sub_array([2, 7, 2, -11, 7], k = 7))
print(max_sub_array([37, 52, 0, 2, 5, 3, 3, 4, 4, 3, 0, 5, 5, 4, 4, 4, 3, 2, 0,
                     2, 3, 1, 3, 0, 4, 3, 1, 4, 5, 2, 4, 3, 1, 4, 5, 0, 3, 4, 0], k=52))
print(max_sub_array([-1, 1, 1], k=1))
print(max_sub_array([1, 2, 1, 0, 1], k=4))
print(max_sub_array([2, 0, 0, 3], k=3))
