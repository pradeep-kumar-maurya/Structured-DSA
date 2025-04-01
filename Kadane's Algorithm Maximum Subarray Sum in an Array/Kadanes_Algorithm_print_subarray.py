def max_subarray_sum(arr):
    '''
    We will use slidind window approach.
    '''
    sum = 0
    max_sum = float('-inf')
    j = -1
    left_most_index = -1
    right_most_index = -1

    for i in range(len(arr)):

        # if sum is <= 0 and arr[i] > 0 then sum should be replaced with arr[i] because a -ve sum + postive arr[i] would
        # still yield in a smaller sum when compared to arr[i]. Hence, replace sum with arr[i]
        if sum <= 0 and arr[i] > 0:
            sum = arr[i]  # whenever sum is set to arr[i], set left_most_index, right_most_index and j to i
            left_most_index = i
            right_most_index = i
            j = i

        # if sum > 0 and adding arr[i] to it is yielding a -ve value, then, replace sum with 0
        elif sum > 0 and sum + arr[i] < 0:
            sum = 0

        # if sum is < 0 and arr[i] is > sum i.e. arr[i] is also a -ve value but greater than the sum, replace sum with arr[i]
        elif sum < 0 and arr[i] > sum:
            sum = arr[i]  # whenever sum is set to arr[i], set left_most_index, right_most_index and j to i
            left_most_index = i
            right_most_index = i
            j = i

        # continue if sum < 0 and arr[i] is < sum i.e. arr[i] is -ve
        elif sum < 0 and arr[i] < sum:
            continue

        # if sum > 0 and sum + arr[i] is also > 0 then add arr[i] to sum, increment j by 1
        else:
            sum += arr[i]
            j += 1

            if left_most_index < 0:  # this will work for only 1 time
                left_most_index += 1

        # whenever sum is > max_sum, set right_most_index to j
        if sum > max_sum:
            max_sum = sum
            right_most_index = j

    return max_sum, arr[left_most_index: right_most_index + 1]


print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray_sum([1]))
print(max_subarray_sum([5,4,-1,7,8]))
print(max_subarray_sum([1, 2, 7, -4, 3, 2, -10, 9, 1]))
print(max_subarray_sum([10, 20, -30, 40, -50, 60]))
print(max_subarray_sum([-3, -5, -6]))
print(max_subarray_sum([-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10])) 

