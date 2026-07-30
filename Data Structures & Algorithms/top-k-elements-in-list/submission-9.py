import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = defaultdict()
        for i in range(len(nums)):
            freqDict[nums[i]] = freqDict.get(nums[i], 0) + 1
        heap = [] #minheap
        for key in freqDict:
            heapq.heappush(heap, (freqDict[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n[1] for n in heap]
        