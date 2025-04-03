def find_majority_element(arr):
    
    ME = arr[0]
    count = 1

    for i in range(1, len(arr)):

        if arr[i] == ME:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            ME = arr[i]
            count += 1

    return ME


print(find_majority_element([3,2,3]))
print(find_majority_element([2,2,1,1,1,2,2]))
print(find_majority_element([4,4,2,4,3,4,4,3,2,4]))
