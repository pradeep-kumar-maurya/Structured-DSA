def find_num(arr):
    XOR = 0

    for num in arr:
        XOR = XOR ^ num

    return XOR


print(find_num([2, 2, 1]))
print(find_num([4, 1, 2, 1, 2]))
