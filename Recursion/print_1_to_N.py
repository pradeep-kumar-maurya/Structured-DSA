def print_nums(N):

    def print_recursive(num):
        if num > N:
            return
        
        print(num)
        num += 1
        print_recursive(num)

    print_recursive(1)


print_nums(5)
