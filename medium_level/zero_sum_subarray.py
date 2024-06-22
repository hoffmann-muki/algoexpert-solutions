# best solution with O(n) time and O(1) space

def zeroSumSubarray(nums):
    n = len(nums)
    if n == 0:
        return False
    if sum(nums) == 0:
        return True
    else:
        partial_sums = set()
        partial_sum = 0
        for i in range(n):
            partial_sum += nums[i]
            if partial_sum in partial_sums:
                return True
            else:
                partial_sums.add(partial_sum)
    return False
