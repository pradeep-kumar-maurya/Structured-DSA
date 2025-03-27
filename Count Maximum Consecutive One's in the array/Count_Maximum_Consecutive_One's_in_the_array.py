def count_ones(prices):
    count = 0
    max_count = 0

    for num in prices:

        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        
        else:
            count = 0

    return max_count


print(count_ones([1, 1, 0, 1, 1, 1]))
print(count_ones([1, 0, 1, 1, 0, 1]))
