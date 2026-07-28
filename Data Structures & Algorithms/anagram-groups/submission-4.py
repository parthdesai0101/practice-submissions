class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            freq = [0] * 26 #represents an alphabet list
            for c in word:
                freq[ord(c) - ord('a')] += 1
            words[tuple(freq)].append(word)
        return list(words.values())