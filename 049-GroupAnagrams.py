class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        result = []
        for str in strs:
            sortedString = "".join(sorted(str))
            if sortedString not in hashMap:
                hashMap[sortedString] = [str]
            else:
                hashMap[sortedString].append(str)

        for val in hashMap.values():
            result.append(val)
        return result

# Another
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for data in strs:
            temp = "".join(sorted(data))
            dic[temp].append(data)
        result = list(dic.values())
        return result