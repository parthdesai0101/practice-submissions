class Solution:
    def isPalindrome(self, s: str) -> bool: # 2 pointer problem
        i,j = 0, len(s) - 1
        while i < j:
            # Skips over the non alphanumeric chars
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1

            # Once there is no alphanumeric char, we do the comparison
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True
        