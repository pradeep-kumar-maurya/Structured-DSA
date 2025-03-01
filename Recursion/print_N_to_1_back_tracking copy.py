def print_nums(i, N):
    if i > N:
        return
    
    print_nums(i + 1, N)  # go till the very last function call and then start printing
    print(i)  # back tracking


print_nums(1, 5)
