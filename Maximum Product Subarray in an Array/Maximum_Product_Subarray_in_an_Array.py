def max_subarray_product(arr):

    '''
    The intuition is to maintain product of the array in each iteration and also maintain the max product in each iteration.
    We will do another iteration over the array but this time we will only consider the product of the consecutive +ve nos and
    maintain another max product.
    At last we will compare both the max products and return the bigger one.
    '''
    product = 1
    max_product1 = float('-inf')
    max_product2 = float('-inf')

    # The below for loop will do a product of the entire array and maintain the max_product1.
    for num in arr:

        if num != 0:

            product = product * num

            if product > max_product1:
                max_product1 = product
            
            elif num > max_product1:
                max_product1 = num
        
        else:
            product = 1

    product = 1  # we will set product to 1 again because we will do one more iteration

    '''
    The below for loop will do a product of only consecutive +ve nos in the array and maintain the max_product2.
    We run this iteration because there can be cases where product of consecutive +ve nos is greater than the product of
    the entire array.
    '''
    for num in arr:

        if num > 0:

            product = product * num

            if product > max_product2:
                max_product2 = product
            
            elif num > max_product2:
                max_product2 = num

        else:
            product = 1

    # return whatever is greater among max_product1 and max_product2
    return max_product1 if max_product1 > max_product2 else max_product2


print(max_subarray_product([1,2,3,4,5,0]))
print(max_subarray_product([1,2,-3,0,-4,-5]))
print(max_subarray_product([-2, 3, -4, 0]))
print(max_subarray_product([1, -2, 3, -4]))
print(max_subarray_product([-1, 3, 0, -4, 3]))
print(max_subarray_product([1, -2, 3, 4]))
print(max_subarray_product([0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 1, 1, -1, 1, 1, -6, 2, 0]))
print(max_subarray_product([8, -1, 1, 1, -9, -1]))
