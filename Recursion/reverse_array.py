def reverse(arr):
    
    # two pointers approach
    
    def recursive_reverse(arr, i, j):
        if i > j:
            return
        
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

        recursive_reverse(arr, i + 1, j - 1)

    recursive_reverse(arr, 0, len(arr) - 1)


arr = [1, 2, 3, 4]
reverse(arr)
print(arr)

arr = [1, 2, 3, 4, 5]
reverse(arr)
print(arr)