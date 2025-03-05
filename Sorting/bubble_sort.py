def bubble_sort(arr):
    '''
    Bubble sort compares two adjacent values at a time and after every single iteration we will have the greatest number
    at the right side of the array.
    Worst case, Average case T.C: O(N^2).
    Best case T.C = O(N) becasue of the already sorted array.
    '''

    is_swapped = False

    for i in range(0, len(arr) - 1, 1):

        for j in range(0, len(arr) - i - 1, 1):

            if arr[j] > arr[j + 1]:  # swap if arr[j] > arr[j + 1]
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

                is_swapped = True  # this will let us know if all the elements are in sorted order after a single for loop run

        if is_swapped == False:
            break
    

arr = [5, 4, 3, 2, 1]
arr = [1, 2, 3]
# arr = [1, 1, 1, 1]
# arr = [1]
# arr = [-3, -100, -2, 1, 0]
bubble_sort(arr)
print(arr)
