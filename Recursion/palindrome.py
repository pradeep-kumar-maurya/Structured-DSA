def palindrome(string):

    # two pointers approach

    def check_palindrome(string, i, j):
        if i > j:
            return True
        
        elif string[i] != string[j]:
            return False
        
        return check_palindrome(string, i + 1, j - 1)

    return check_palindrome(string, 0, len(string) - 1)


print(palindrome("aaabaaa"))
print(palindrome("aaabaa"))
print(palindrome("1221"))
