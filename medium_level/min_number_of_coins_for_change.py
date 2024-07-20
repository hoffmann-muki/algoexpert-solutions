# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    min_coins = [0 for amount in range(n+1)]
    min_coins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if amount >= denom:
                if amount == denom:
                    min_coins[amount] = 1
                else:
                    if min_coins[amount] > 0:
                        if min_coins[amount - denom] > 0:
                            min_coins[amount] = min(min_coins[amount], 1 + min_coins[amount - denom]) 
                    else:
                        if min_coins[amount - denom] == 0:
                            min_coins[amount] == 0
                        else:
                            min_coins[amount] = 1 + min_coins[amount - denom]
    if min_coins[n] > 0:
        return min_coins[n]
    else:
        if n == 0:
            return 0
        return -1
