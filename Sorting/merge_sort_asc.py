def merge(arr, start, mid, end):
    temp = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:  # ascending order will be "<="
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    for i in range(len(temp)):
        arr[i + start] = temp[i]


# Best, Average, Worst T.C = O(N * (log N base to 2)), S.C = O(N) because of temp array while merging
def mergre_sort(arr, start, end):
    # if start == end:  # base case 1
    #     return

    # if start >= end:  # base case 2
    #     return

    if start < end:  # base case 3
        mid = (start + end) // 2

        mergre_sort(arr, start, mid)  # 1st -> keep on dividing the left part of the array until it has only one element left
        mergre_sort(arr, mid + 1, end)  # 2nd -> Once we have only one element at the left, we will also have one element in the right
        merge(arr, start, mid, end)  # just merge the two subarrays and place it at the correct position in the original array


arr = [5, 4, 3, 2, 1]
mergre_sort(arr, 0, len(arr) - 1)
print(arr)
