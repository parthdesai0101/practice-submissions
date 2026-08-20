class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) - 1
        while i < j:
            if (numbers[i] + numbers[j]) > target:
                j -= 1
            elif numbers[i] + numbers[j] == target:
                break
            else:
                i += 1
        return [i + 1, j + 1]

        