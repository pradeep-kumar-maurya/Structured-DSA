def alternateNumbers(arr):

    positive_arr = []
    negative_arr = []
    final_arr = []

    for num in arr:

        if num > 0:
            positive_arr.append(num)
        else:
            negative_arr.append(num)

    for i in range(len(positive_arr)):
        final_arr.extend([positive_arr[i], negative_arr[i]])

    return final_arr


print(alternateNumbers([1, 2, -4, -5]))
print(alternateNumbers([1, 2, -3, -1, -2, 3]))
