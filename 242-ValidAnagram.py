class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMapS = {}
        for num in s:
            if num not in hashMapS:
                hashMapS[num] = 1
            else:
                hashMapS[num] += 1

        hashMapT = {}
        for num in t:
            if num not in hashMapT:
                hashMapT[num] = 1
            else:
                hashMapT[num] += 1

        return hashMapS == hashMapT

# another approach (better in memory usage)
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        # Count every character in s
        for char in s:
            count[char] += 1

        # Subtract every character in t
        for char in t:
            count[char] -= 1

            # If a character appears more times in t than s
            if count[char] < 0:
                return False

        return True