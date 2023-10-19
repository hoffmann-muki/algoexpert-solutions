def minimumWaitingTime(queries):
    queries.sort()
    sum = 0
    n = len(queries)
    for i in range(n):
        sum += (n-1-i) * queries[i]
    return sum
