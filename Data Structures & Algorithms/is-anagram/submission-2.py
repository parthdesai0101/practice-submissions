class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range(0, len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
        for j in range(0, len(t)):
            if t[j] not in t_dict:
                t_dict[t[j]] = 1
            else:
                t_dict[t[j]] += 1
        return s_dict == t_dict