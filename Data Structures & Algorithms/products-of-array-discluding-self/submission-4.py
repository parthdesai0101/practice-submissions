class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix, postfix = 1, 1 #always intialize 1 since start and end have no pre/post entry

        for i in range(len(nums)):
            res[i] = prefix #set entry to prefix
            prefix *= nums[i] #update prefix by mul by current entry in list
        
        for i in range(len(nums) - 1, -1, -1): #decsending order
            res[i] *= postfix #take prefix and mul by postfix
            postfix *= nums[i] #update postfix by mul current entry
        return res

        

        