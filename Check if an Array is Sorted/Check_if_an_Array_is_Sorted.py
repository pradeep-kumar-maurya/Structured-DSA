def check_sorted(arr) -> bool:
    if_increasing = False
    if_decreasing = False

    for i in range(len(arr) - 1):
        if arr[i] - arr[i + 1] < 0:
            if_increasing = True
        
        else:
            if_decreasing = True

    if if_increasing and if_decreasing:
        return False
    
    else:
        return True


arr = [1, 2, 3, 4, 5]
arr = [5, 4, 6, 7, 8]
arr = [5, 4, 3, 2, 1]
print(check_sorted(arr))

