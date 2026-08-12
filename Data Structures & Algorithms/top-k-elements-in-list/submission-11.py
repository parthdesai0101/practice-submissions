import heapq #min heap by default
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for i in range(len(nums)):
            freqDict[nums[i]] = freqDict.get(nums[i], 0) + 1
        heap = []
        for key in freqDict:
            heapq.heappush(heap, (freqDict[key], key)) #heap contains num occurences at index 0 followed by num itself at index 1
            if len(heap) > k:
                heapq.heappop(heap) # we pop the smallest occurring element
        return [n[1] for n in heap]
