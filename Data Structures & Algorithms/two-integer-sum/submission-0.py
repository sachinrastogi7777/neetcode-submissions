class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target not in seen:
                seen[nums[i]] = i
            else:
                return [seen[new_target], i]