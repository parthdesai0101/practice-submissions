class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        for word in strs:
            sWord = "".join(sorted(word))
            if sWord in wordDict:
                wordDict[sWord].append(word)
            else:
                wordDict[sWord] = [word]
        return list(wordDict.values())