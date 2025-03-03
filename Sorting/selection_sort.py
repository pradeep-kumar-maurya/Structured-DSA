def selection_sort(arr):

    '''
    In selection sort, we choose the smallest element and swap it with the 1st element in the array. Then we again find the smallest
    no. in the array starting from (i + 1) till the last index and swap it with the 2nd element in the array. This keeps on going
    until index i reaches the 2nd last index.
    '''

    for i in range(0, len(arr) - 1, 1):  # i goes from 0 to N-2

        min_index = i

        for j in range(i, len(arr), 1):  # j goes from 0 to N-1

            if arr[j] < arr[min_index]:
                min_index = j

        # we can always perform a swap no matter what
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp


arr = [0, -1, -100, 2, -4]
arr = [5, 4]
arr = [1]
arr = [5, 4, 3, 2, 1, 0]
arr = [1, 1, 1, 1, 1]
selection_sort(arr)
print(arr)

