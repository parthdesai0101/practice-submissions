class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        longest = 0

        for num in nums:
            # check if it's the start of a sequence
            if (num - 1) not in visited:
                length = 0
                while (num + length) in visited:
                    length += 1
                longest = max(length, longest)
        return longest
        


        