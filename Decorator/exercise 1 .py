''''
def check(nums: list[int], k: int) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False

nums = [2, 7, 11, 15]
k = 9

print(check(nums, k))

'''

def get_nums(nums: list[int]):
    for x in set(nums):
        if nums.count(x) == 1:
            return x
    return None

print(get_nums([1, 1, 2, 2, 3, 3]))
