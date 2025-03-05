def merge(arr, start, mid, end):
    temp = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if arr[i] >= arr[j]:  # descending order will be ">="
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


def mergre_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        mergre_sort(arr, start, mid)
        mergre_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


arr = [1, 2, 3, 4, 5]
mergre_sort(arr, 0, len(arr) - 1)
print(arr)
