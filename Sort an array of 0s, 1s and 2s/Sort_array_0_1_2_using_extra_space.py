def sort_array(arr):

    freq_dict = {}

    for num in arr:

        if freq_dict.get(num) is None:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

    k = 0

    for i in range(3):
        if freq_dict.get(i):
            for _ in range(freq_dict.get(i)):
                arr[k] = i
                k += 1

arr = [0, 1, 2, 2, 1, 0]
sort_array(arr)
print(arr)

arr = [2, 0, 1]
sort_array(arr)
print(arr)

arr = [0]
sort_array(arr)
print(arr)
