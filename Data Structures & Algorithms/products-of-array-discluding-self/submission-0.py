class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n #[1, 0, 0, 0]
        postfix = [0] * n #[0, 0, 0, 1]

        prefix[0] = postfix[n - 1] = 1 # set to one since pre and post have no precursor or postcursors
        for i in range(1, n): #prefix
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1): #postfix
            postfix[i] = nums[i + 1] * postfix[i + 1]
        
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
        return res