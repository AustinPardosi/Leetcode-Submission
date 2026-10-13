class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        data = set()

        for r, char in enumerate(s):
            while char in data:
                data.remove(s[l])
                l += 1
            data.add(char)
            length = max(r-l+1,length)
        return length