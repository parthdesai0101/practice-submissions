from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)
        for word in strs:
            sWord = "".join(sorted(word))
            wordDict[sWord].append(word)
        return list(wordDict.values())