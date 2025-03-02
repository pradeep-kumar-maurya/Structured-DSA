#  ----------------------------------- RECURSION -----------------------------------------
def fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    return fibonacci(N - 1) + fibonacci(N - 2)


# print(fibonacci(4))
#  ----------------------------------- RECURSION -----------------------------------------


#  ------------------------------ RECURSION MEMOIZATION ----------------------------------
memoization_dict = {}  # store the fibonacci function call value for N

def fibonacci(N):
    global memoization_dict

    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    if memoization_dict.get(N):  # no need to iterate over and over again if it's already done
        return memoization_dict[N]

    else:
        last = fibonacci(N - 1)
        second_last = fibonacci(N - 2)
        memoization_dict[N] = last + second_last  # add the fibnonacci(N) value to the memoization dict for faster execution 

    return memoization_dict[N]  # OR we can also return (last + second_last)


print(fibonacci(50))
#  ------------------------------ RECURSION MEMOIZATION ----------------------------------


#  ----------------------------------- FOR LOOP -----------------------------------------
def fibonacci(N):

    fib_arr = []

    for i in range(N + 1):

        if i == 0:
            fib_arr.append(i)

        elif i == 1:
            fib_arr.append(i)

        else:
            num = fib_arr[i - 1] + fib_arr[i - 2]
            fib_arr.append(num)

    return fib_arr[-1]


print(fibonacci(50))
#  ----------------------------------- FOR LOOP -----------------------------------------

