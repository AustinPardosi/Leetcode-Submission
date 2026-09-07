from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.data = defaultdict(list)
        self.n = len(wordsDict)
        for i, word in enumerate(wordsDict):
            self.data[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        dict1, dict2 = self.data[word1], self.data[word2]
        distance = self.n
        i, j = 0, 0
        while i < len(dict1) and j < len(dict2):
            distance = min(distance, abs(dict1[i]-dict2[j]))
            if distance == 1:
                return 1
            if dict1[i] < dict2[j]:
                i += 1
            else:
                j += 1
        return distance
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)