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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        data = {}

        for num in s:
            data[num] = data.get(num, 0) + 1
        for num in t:
            if num not in data:
                return False
            data[num] -= 1
            if data[num] == 0:
                del data[num]

        return True