def findMissingRepeatingNumbers(arr):
    '''
    We can store the frequency of all the elements in a dict and whatever element appears twice should be appended to the ans
    array. Later, we will run a while loop from 1 to N and check in the frequency dict and the missing element will be appended
    to the ans array.
    '''
    freq_dict = {}
    ans = []
    i = 1

    for num in arr:
        
        if freq_dict.get(num) is None:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
            ans.append(num)

    while i <= len(arr):

        if freq_dict.get(i) is None:
            ans.append(i)
            break

        i += 1

    return ans


print(findMissingRepeatingNumbers([1, 2, 3, 2]))
print(findMissingRepeatingNumbers([3, 1, 2, 5, 3]))
print(findMissingRepeatingNumbers([3, 1, 2, 5, 4, 6, 7, 5]))
print(findMissingRepeatingNumbers([9, 7, 13, 1, 15, 18, 17, 8, 4, 19, 10, 5, 3, 11, 2, 12, 15, 14, 16, 6]))
