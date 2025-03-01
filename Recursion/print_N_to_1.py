def print_nums(N):

    def print_recursive(num):
        if num < 1:
            return
        
        print(num)
        num -= 1
        print_recursive(num)
    
    print_recursive(N)


print_nums(5)
