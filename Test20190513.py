
nums = [2, 11, 7, 15]
target = 9


def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum(nums, target))

