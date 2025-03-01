def print_nums(N):
    if N < 1:
        return
    
    print_nums(N - 1)  # go till the very last function call and then start printing
    print(N)  # back tracking


print_nums(5)
