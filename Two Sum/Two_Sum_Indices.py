def two_sum(arr, target):
    
    freq_dict = {}

    for i, num in enumerate(arr):

        if freq_dict.get(num) is None:
            freq_dict[num] = [i]
        else:
            freq_dict[num].append(i)

    for num in arr:

        diff = target - num

        if freq_dict.get(diff) is not None:

            if diff == num:  # check if frequency is > 1 if same no. is used twice to get the sum
                if len(freq_dict.get(diff)) > 1:
                    return freq_dict.get(diff)
            else:
                return [freq_dict.get(num)[0], freq_dict.get(diff)[0]]

    return [-1, -1]


print(two_sum([2, 6, 5, 8, 11], target=14))
print(two_sum([2, 6, 5, 8, 11], target=15))
print(two_sum([2, 6, 5, 7, 11], target=10))
print(two_sum([2, 6, 5, 7, 11, 5], target=10))
