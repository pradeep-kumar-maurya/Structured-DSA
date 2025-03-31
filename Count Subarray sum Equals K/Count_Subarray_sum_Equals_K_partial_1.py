'''
This solution works for only +ve elements.
'''
def count_subarray(arr, k):

    i = 0
    count = 0
    sum = 0

    for j in range(len(arr)):

        sum += arr[j]

        if sum > k:
            while i < j and sum > k:
                sum -= arr[i]
                i += 1

        if sum == k:
            count += 1
    
    return count


# print(count_subarray([3, 1, 2, 4], 6))
# print(count_subarray([1, 2, 3], 3))
# print(count_subarray([1], 0))
print(count_subarray([-1, -1, 1], 0))
print(count_subarray([0, 0, 0, 3], 3))
