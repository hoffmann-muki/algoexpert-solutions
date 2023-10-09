import itertools

############ Brute force solution ##############
def nonConstructibleChange(coins):
    sums = set()
    if not coins:
        return 1
    else:
        for r in range(1, len(coins)+1):
          r_combinations = itertools.combinations(coins, r)
          r_sums = [sum(x) for x in r_combinations]
          sums.update(r_sums)
    sorted_sums = sorted(sums, reverse=True)
    max_sum = sorted_sums[0]
    for possible_sum in range(1, max_sum+2):
        if possible_sum not in sorted_sums:
            return possible_sum

############ Optimal solution ################
def nonConstructibleChange(coins):
    current_change = 0
    coins.sort()
    for i in range(len(coins)):
        if coins[i] > (current_change+1):
            return current_change+1
        current_change += coins[i]
    return current_change+1

