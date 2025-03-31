def sequence(arr):
    '''
    The idea is to create an arr_set of arr and then iterate over the arr_set. We will only bother about the elements right to
    each num in the arr_set. If num - 1 is already there in the arr_set, we will skip and go to other num because there can be
    a num in the arr set, which if incremented by 1 every time, would lead to the consecuive elements that will cover the
    num - 1 th element too.
    '''

    arr_set = set()
    max_size = 0

    for num in arr:
        arr_set.add(num)
    
    for num in arr_set:

        size = 0

        if num - 1 not in arr_set:  # if num-1 is not there in the arr_Set then only start incrementing the num by 1

            size += 1

            while num + 1 in arr_set:  # while loop checks for all the consecutive elements right to the num
                size += 1
                num += 1

            if size > max_size:
                max_size = size
    
    return max_size


print(sequence([100, 200, 1, 3, 2, 4]))
print(sequence([3, 8, 5, 7, 6]))
print(sequence([5, 8, 3, 2, 1, 4]))
