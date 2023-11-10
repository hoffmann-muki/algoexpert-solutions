# Recursive solution
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

# Iterative solution
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        sum = 0
        a, b = 0, 1
        for i in range(3, n+1):
            sum = a + b # fib(n+1)
            a = b # a = fib(n-1)
            b = sum # b = fib(n)
        return sum
