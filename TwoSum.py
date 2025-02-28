class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in dictionary:
                return [dictionary[diff], i]

            dictionary[num] = i
        #return None

    # nums = sorted(nums)
    # left = 0
    # right = len(nums) - 1

    # while left < right:
    #     total = nums[left] + nums[right]

    #     if total == target:
    #         return left, right
    #     elif total < target:
    #         left += 1
    #         #right = right + 1
    #     else:
    #         right -= 1
