def max_subarray_sum(arr):
    '''
    We will use slidind window approach.
    '''
    sum = 0
    max_sum = float('-inf')

    for i in range(len(arr)):

        # if sum is <= 0 and arr[i] > 0 then sum should be replaced with arr[i] because a -ve sum + postive arr[i] would
        # still yield in a smaller sum when compared to arr[i]. Hence, replace sum with arr[i]
        if sum <= 0 and arr[i] > 0:
            sum = arr[i]

        # if sum > 0 and adding arr[i] to it is yielding a -ve value, then, replace sum with 0
        elif sum > 0 and sum + arr[i] < 0:
            sum = 0

        # if sum is < 0 and arr[i] is > sum i.e. arr[i] is also a -ve value but greater than the sum, replace sum with arr[i]
        elif sum < 0 and arr[i] > sum:
            sum = arr[i]

        # if sum > 0 and sum + arr[i] is also > 0 then add arr[i] to sum
        else:
            sum += arr[i]

        if sum > max_sum:
            max_sum = sum

    return max_sum


# print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
# print(max_subarray_sum([1]))
# print(max_subarray_sum([5,4,-1,7,8]))
# print(max_subarray_sum([1, 2, 7, -4, 3, 2, -10, 9, 1]))
# print(max_subarray_sum([10, 20, -30, 40, -50, 60]))
print(max_subarray_sum([-3, -5, -6]))
print(max_subarray_sum([-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10])) 

