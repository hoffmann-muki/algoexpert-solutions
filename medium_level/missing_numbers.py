# solution with O(n) time and O(n) space

def missingNumbers(nums):
    n = len(nums) + 2
    s = set(nums)
    missing = []
    for i in range(1, n+1):
        if i not in s:
            missing.append(i)
    return missing

# best solution: O(n) time and O(1) space

def missingNumbers(nums):
    size = len(nums)
    n = size + 2
    sum_of_nums = sum(nums)
    sum_of_n = n*(n+1)/2
    diff = sum_of_n - sum_of_nums
    avg = diff // 2
    sum_left_half = avg*(avg+1)/2
    sum_right_half = sum_of_n - sum_left_half
    # one number is less than avg, the other greater than avg
    left_sum, right_sum = 0, 0
    for i in range(size):
        if nums[i] <= avg:
            left_sum += nums[i]
        else:
            right_sum += nums[i]
    missing_left = sum_left_half - left_sum
    missing_right = sum_right_half - right_sum
    # order the results
    smaller = missing_left if missing_left < missing_right else missing_right
    bigger = (missing_left + missing_right) - smaller
    return [smaller, bigger]
