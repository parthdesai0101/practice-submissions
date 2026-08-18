class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            res[i] = prefix #set the first entry equal to the prefix, then we must update the prefix by the current number value
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # need to multiple the prefix by the postfix
            postfix *= nums[i] #update the postfix value by the current entry
        return res