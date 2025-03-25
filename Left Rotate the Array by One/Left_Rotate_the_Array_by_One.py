def rotate(arr):
    
    for i in range(0, len(arr) - 1):

        # The approach is to use two pointers and swap consecutive elements from left to right
        temp = arr[i + 1]
        arr[i + 1] = arr[i]
        arr[i] = temp


arr = [1,2,3,4,5]
arr = [3]
rotate(arr)
print(arr)
