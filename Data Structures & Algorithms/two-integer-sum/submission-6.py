class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = defaultdict(int)
        for i, n in enumerate(nums):
            prevMap[n] = i

        for i, n in enumerate(nums):
            complement = target - nums[i]
            print(complement)
            if complement in prevMap and prevMap[complement] != i:
                return [i, prevMap[complement]]
        return []
        