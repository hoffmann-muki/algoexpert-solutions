def isPalindrome(string):
    n = len(string)
    if n == 1:
        return True
    else:
        mid = n // 2 if n % 2==0 else (n // 2)+1
        for i in range(mid):
            forward_ptr = string[i]
            backward_ptr = string[n-1-i]
            if forward_ptr != backward_ptr:
                return False
        return True
