def print_name(string, N):

    def print_recursive(string, num):
        if num > N:
            return
        
        print(string)
        num += 1
        print_recursive(string, num)

    print_recursive(string, 1)  # recursive call


print_name("python", 5)
