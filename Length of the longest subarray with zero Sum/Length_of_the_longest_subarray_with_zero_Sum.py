def find_longest_zero_subarray(arr):
    
    '''
    The intuition is to find the prefix sum and then store all the indices of prefix sums in a dict where value will be a list
    of indices. To have a subarray with sum as 0, there should be repeating prefix sums. Therefore, if there is a prefix sum
    in the dict with len of value as > 1 then we just need to subtract the first index from the last index to get the max size
    of the subarray with sum as 0. If there is a 0 in the dict then we simply need to add 1 to the last index at which 0 appeared.
    '''
    prefix_sum = 0
    prefix_freq_dict = {}
    max_subarray_length = 0

    # to maintain all the indices of all the prefix sums
    for i in range(len(arr)):

        prefix_sum += arr[i]

        if prefix_freq_dict.get(prefix_sum) is None:
            prefix_freq_dict[prefix_sum] = [i]
        else:
            prefix_freq_dict[prefix_sum].append(i)

    for key, value in prefix_freq_dict.items():

        if key == 0:  # if key is 0 then we simply need to add 1 to the last index of 0
            subarray_length = value[-1] + 1
            if subarray_length > max_subarray_length:
                max_subarray_length = subarray_length

        elif len(value) > 1:  # if len of value is > 1 then we simply need to subtract first index from the last index
            subarray_length = value[-1] - value[0]

            if subarray_length > max_subarray_length:
                max_subarray_length = subarray_length
    
    return max_subarray_length


print(find_longest_zero_subarray([9, -3, 3, -1, 6, -5]))
print(find_longest_zero_subarray([6, -2, 2, -8, 1, 7, 4, -10]))
print(find_longest_zero_subarray([1, 0, -5]))
print(find_longest_zero_subarray([1, 3, -5, 6, -2]))
print(find_longest_zero_subarray([1, 0,-1, 1]))
print(find_longest_zero_subarray([1, 1]))
print(find_longest_zero_subarray([1, -1, 0, 0, 2]))
