count = 0

def print_count():
    global count
    
    if count == 5:
        return
    
    print(count)
    count += 1

    print_count()  # recursive call


print_count()
