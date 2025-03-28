def stock(arr):

    max_profit = 0
    max_element = arr[-1]

    for i in range(len(arr) - 1, -1, -1):

        if arr[i] > max_element:
            max_element = arr[i]
        
        diff = max_element - arr[i]

        if diff > max_profit:
            max_profit = diff
    
    return max_profit


print(stock([7, 1, 5, 3, 6, 4]))
print(stock([7, 6, 4, 3, 1]))
print(stock([2, 100, 150, 120]))
print(stock([1, 2, 3, 4]))
print(stock([2, 2, 2, 2]))
print(stock([17, 20, 11, 9, 12, 6]))
print(stock([98, 101, 66, 72]))
