def sort_array(arr):
    # We are using bubble sort

    length = len(arr)

    for _ in range(len(arr)):

        m = 0
        n = m + 1

        while n < length:

            if arr[m] > arr[n]:  # swap

                temp = arr[n]
                arr[n] = arr[m]
                arr[m] = temp

            m += 1
            n += 1

        # (length - 1) is used to avoid extra iterations because after every iteration, the max no. will be at the end
        length -= 1


arr = [2, 0, 2, 1, 1, 0]
sort_array(arr)
print(arr)

arr = [2, 0, 1]
sort_array(arr)
print(arr)

arr = [0]
sort_array(arr)
print(arr)
