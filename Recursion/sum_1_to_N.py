def find_sum(N):
    if N == 0:
        return 0

    return N + find_sum(N - 1)
    
    
print(find_sum(5))

# ------------------------------- ALTERNATE -----------------------------------

def find_sum(N):
    def recursive_sum(sum, N):
        if N == 0:
            return sum
        
        sum += N
        return recursive_sum(sum, N - 1)
    
    return recursive_sum(0, N)
    
print(find_sum(3))
