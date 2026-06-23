class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in mp:
                return [mp[rem], i]

            mp[nums[i]] = i
