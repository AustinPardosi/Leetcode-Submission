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
