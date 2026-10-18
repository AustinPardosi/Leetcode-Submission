class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # Count odd-length palindromes centered at i
            count += self.expand(s, i, i)
            # Count even-length palindromes centered between i and i+1
            count += self.expand(s, i, i+1) # for even
        return count
    
    def expand(self, s, l, r):
        count = 0

        # Keep expanding while the characters match
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1 # Found one palindrome
            l -= 1
            r += 1
        return count