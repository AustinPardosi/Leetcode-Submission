class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def findAll(word) -> List[int]:
            result = []
            idx = s.find(word)
            while idx != -1:
                result.append(idx)
                idx = s.find(word, idx+1)
            return result

        A, B = findAll(a), findAll(b)
        indices, check = [], 0
        for i in A:
            while check < len(B) and (B[check]<i-k):
                check += 1
            if check < len(B) and (B[check]<=k+i):
                indices.append(i)
        return indices