class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = i # pointer to start iterating at
            while s[j] != '#':
                j += 1
            print(i, j)
            
            length = int(s[i:j])
            print(length)
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
