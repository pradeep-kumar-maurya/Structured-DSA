def leader(arr):

    ans = [arr[-1]]
    max = arr[-1]

    for i in range(len(arr) - 2, -1, -1):

        if arr[i] > max:
            max = arr[i]
            ans.append(max)

    i = 0
    j = len(ans) - 1

    while i <= j:
        temp = ans[j]
        ans[j] = ans[i]
        ans[i] = temp
        i += 1
        j -= 1

    return ans


print(leader([4, 7, 1, 0]))
print(leader([1, 2, 3, 2]))
print(leader([1, 2, 2, 1]))
print(leader([10, 22, 12, 3, 0, 6]))
