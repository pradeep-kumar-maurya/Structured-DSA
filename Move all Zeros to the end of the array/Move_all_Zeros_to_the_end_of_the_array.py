def move(arr):

    i = 0
    index_of_zero_element = None

    ''' The idea is to keep an index i.e. index_of_zero_element at 0th element and as soon as we find a non-zero element
    to its right, we need to swap the nos and and increase the index_of_zero_element by 1. '''

    while i < len(arr):
        if arr[i] == 0:
            if index_of_zero_element is None:  # this is one time activity where we grab the 1st 0th element index
                index_of_zero_element = i

        elif index_of_zero_element is not None:
            # swap
            temp = arr[index_of_zero_element]
            arr[index_of_zero_element] = arr[i]
            arr[i] = temp

            # increment index_of_zero_element by 1 so that it points to next 0th element that needs to be swapped
            index_of_zero_element += 1

        i += 1



arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
arr = [1, 2, 0, 1, 0, 4, 0]
arr = [1, 2, 0, 0, 2, 3]
arr = [0, 0, 0, 1, 0, 0, 0]
arr = [0, 1, 2, 3, 4]
move(arr)
print(arr)

