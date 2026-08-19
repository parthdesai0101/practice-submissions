from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list) #if no entry then creates one automatically
        for word in strs:
            sWord = "".join(sorted(word))
            wordDict[sWord].append(word)
        return list(wordDict.values())