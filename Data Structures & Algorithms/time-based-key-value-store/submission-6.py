class TimeMap:

    def __init__(self):
        self.entries = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.entries[key].append([key, value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.entries[key]

        #binary search time
        l,r = 0, len(vals) - 1
        while l <= r:
            mid = (l + r) // 2
            if vals[mid][2] <= timestamp:
                res = vals[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
                
