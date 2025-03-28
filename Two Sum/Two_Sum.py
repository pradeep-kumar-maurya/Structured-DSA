def two_sum(arr, target):
    
    freq_dict = {}

    for num in arr:

        if freq_dict.get(num) is None:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

    for num in arr:

        diff = target - num

        if freq_dict.get(diff) is not None:

            if diff == num:  # check if frequency is > 1 if same no. is used twice to get the sum
                if freq_dict.get(diff) > 1:
                    return 'YES'
            else:
                return 'YES'

    return 'NO'


print(two_sum([2, 6, 5, 8, 11], target=14))
print(two_sum([2, 6, 5, 8, 11], target=15))
print(two_sum([2, 6, 5, 7, 11], target=10))
print(two_sum([2, 6, 5, 7, 11, 5], target=10))
