def nextPermutation(arr):

    k = 0
    is_break = False

    for i in range(len(arr) - 1, 0, -1):

        if arr[i] < arr[i - 1] :
            k = i - 1
            while k >= 0:
                if arr[k] < arr[i]:
                    is_break = True
                    break
                k -= 1
        
        if is_break:
            for i in range(i, k, -1):
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
            return

        if arr[i] > arr[i - 1] and is_break is False:
            temp = arr[i - 1]
            arr[i - 1] = arr[i]
            arr[i] = temp
            return

    # ---------------- Reverse the whole array in cases where no next greater arrangement is possible ---------------
    i = 0
    j = len(arr) - 1

    while i <= j:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

        i += 1
        j -= 1
    # ---------------- Reverse the whole array in cases where no next greater arrangement is possible ---------------


# arr = [1, 3, 2]
# nextPermutation(arr)
# print(arr)

# arr = [1, 2, 4, 3]
# nextPermutation(arr)
# print(arr)

arr = [2, 3, 1]
nextPermutation(arr)
print(arr)

arr = [1, 3, 4, 5, 2]
nextPermutation(arr)
print(arr)

arr = [1, 3, 4, 3, 2]
nextPermutation(arr)
print(arr)

# arr = [3, 2, 1]
# nextPermutation(arr)
# print(arr)

# arr = [1, 1, 5]
# nextPermutation(arr)
# print(arr)

# arr = [1]
# nextPermutation(arr)
# print(arr)
