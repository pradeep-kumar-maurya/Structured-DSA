def merge_intervals(arr):
    
    index = 0
    i = 0
    max = arr[0][1]
    ans = []

    while i <= len(arr) - 2:

        if max >= arr[i + 1][0]:
            if arr[i + 1][1] >= max:
                max = arr[i + 1][1]
            i += 1

        else:
            ans.append([arr[index][0], arr[i][1]])
            i += 1
            index = i
            max = arr[i][1]

    if index != len(arr) - 1:
        ans.append([arr[index][0], arr[-1][1]])
    
    else:
        ans.append(arr[index])

    return ans


print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[1, 3], [2, 4], [3, 5], [6, 7]]))
print(merge_intervals([[1, 2], [1, 3], [1, 6], [3, 4], [4, 4], [4, 5], [5, 5], [6, 6], [6, 6]]))
print(merge_intervals([[2,2],[2,3],[2,5],[3,6],[4,4],[4,5],[5,6]]))
print(merge_intervals([[1,4],[3,3],[3,3],[3,3],[3,4],[4,4],[5,5],[5,5],[5,6]]))
