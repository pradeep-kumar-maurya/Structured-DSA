def sort_array(arr):

    # We will use Dutch National Flag Algorithm which uses 3 pointers to sort the array within O(N) TC and O(1) SC.
    # Youtube link for the visualization of the algorithm: https://www.youtube.com/watch?v=9pdkbqGwUhs

    low = 0
    mid = 0
    high = len(arr) - 1

    # The loop has to run until mid <= high because once mid crosses the high pointer, the array will be sorted
    while mid <= high:

        # Whenever arr[mid] == 0 i.e. the lowest element, swap it with arr[low] and increment both low and mid pointer by 1
        if arr[mid] == 0:

            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp

            low += 1
            mid += 1

        # Whenever arr[mid] == 1 i.e. the middle element, just increment mid pointer by 1
        elif arr[mid] == 1:

            mid += 1

        # Whenever arr[mid] == 2 i.e. the highest element, swap arr[mid] with arr[high] and just decrement high by 1
        elif arr[mid] == 2:

            temp = arr[high]
            arr[high] = arr[mid]
            arr[mid] = temp

            high -= 1



arr = [0, 1, 2, 2, 1, 0]
sort_array(arr)
print(arr)

arr = [2, 0, 1]
sort_array(arr)
print(arr)

arr = [0]
sort_array(arr)
print(arr)

arr = [2, 0, 2, 1, 1, 0]
sort_array(arr)
print(arr)

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]
sort_array(arr)
print(arr)
