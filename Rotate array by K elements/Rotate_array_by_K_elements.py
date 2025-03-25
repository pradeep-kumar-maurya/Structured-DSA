def rotate_array(arr, k):
    
    # ---------------------- Reverse the entire array ---------------------
    i = 0
    j = len(arr) - 1
    while i <= j:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1
    # ---------------------- Reverse the entire array ---------------------

    # ------------- Reverse the array from index 0 till k - 1 -------------
    i = 0
    j = k - 1
    while i <= j:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1
    # ------------- Reverse the array from index 0 till k - 1 -------------

    # ------------- Reverse the array from index k till N - 1 -------------
    i = k
    j = len(arr) - 1
    while i <= j:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1
    # ------------- Reverse the array from index k till N - 1 -------------


arr = [1, 2, 3, 4, 5, 6, 7]
arr = [3,7,8,9,10,11]
rotate_array(arr, 3)
print(arr)

