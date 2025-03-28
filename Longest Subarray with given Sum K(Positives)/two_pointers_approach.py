'''
This approach works for all +ve values, might work for cases with 0's and -ve nos but can't commit.
'''

def max_sub_array(arr, k):

    index = 0
    i = 0
    max_size = 0
    sum = 0

    while i < len(arr):

        sum += arr[i]

        if sum > k:
            while index <= i and sum > k:
                sum -= arr[index]
                index += 1

        if sum == k:
            if i - index + 1 > max_size:
                max_size = i - index + 1
            
        i += 1

    return max_size


# print(max_sub_array([2, 3, 5], k = 5))
# print(max_sub_array([2, 3, 5, 1, 9], k = 10))
print(max_sub_array([2, 7, 2, -11, 7], k = 7))
# print(max_sub_array([37, 52, 0, 2, 5, 3, 3, 4, 4, 3, 0, 5, 5, 4, 4, 4, 3, 2, 0,
                    #  2, 3, 1, 3, 0, 4, 3, 1, 4, 5, 2, 4, 3, 1, 4, 5, 0, 3, 4, 0], k=52))
# print(max_sub_array([-1, 1, 1], k=1))
# print(max_sub_array([1, 2, 1, 0, 1], k=4))
# print(max_sub_array([2, 0, 0, 3], k=3))
