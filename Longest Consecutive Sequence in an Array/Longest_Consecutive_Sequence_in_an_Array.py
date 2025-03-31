def sequence(arr):
    '''
    The idea is to create two sets. One set will store the elements from the arr and the other set will store the consecutive
    elements from the arr. If element is already present in the consecutve set then skip that element. If not, first go through
    all the elements left to the current element and check if they are all there in the arr set and then go through all the
    elements right to the current element and check if they are all there in the arr set. All these left and right elments
    will be added in the consecutive set.
    '''
    arr_set = set()
    consecutive_set = set()
    max_size = 0

    for num in arr:
        arr_set.add(num)  # create the arr set

    for num in arr:

        temp1 = num
        temp2 = num
        size = 0

        # go through all the elements left to the current num and all the left elements must be present in the array set but
        # not present in the consecutive_set
        while ((temp1 - 1) in arr_set) and ((temp1 - 1) not in consecutive_set):
            size += 1
            consecutive_set.add(temp1 - 1)  # keep on adding elements to the consecutive set
            temp1 -= 1

        # go through all the elements right to the current num and all the right elements must be present in the array set but
        # not present in the consecutive_set
        while ((temp2 + 1) in arr_set) and ((temp2 + 1) not in consecutive_set):
            size += 1
            consecutive_set.add(temp2 + 1)  # keep on adding elements to the consecutive set
            temp2 += 1
        
        if size + 1 > max_size:
            max_size = size + 1

    return max_size


print(sequence([100, 200, 1, 3, 2, 4]))
print(sequence([3, 8, 5, 7, 6]))
print(sequence([5, 8, 3, 2, 1, 4]))

