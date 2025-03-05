def insertion_sort(arr):
    '''
    In insertion sort, we take one element at a time and then find it's appropriate position in the final sorted array by comparing
    it with all the values to its left side.
    Worst, Average T.C: O(N^2).
    Best T.C: O(N) if the array is already sorted.
    '''

    for i in range(0, len(arr) - 1, 1):

        j = i + 1

        while j > 0:

            if arr[j] < arr[j - 1]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp

            else:
                break

            j -= 1


arr = [5, 4, 3, 2, 1]
arr = [1, 2, 3]
arr = [1, 1, 1, 1]
arr = [1]
arr = [-3, -100, -2, 1, 0]

insertion_sort(arr)
print(arr)

