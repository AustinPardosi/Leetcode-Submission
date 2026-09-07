class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parents = list(range(n))

        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]

        def union(a, b):
            parents[find(a)] = find(b)
        
        # Create Union Find
        for pair in pairs:
            union(pair[0], pair[1])
        
        # Find Groups
        data = defaultdict(list)
        for i in range (len(parents)):
            data[find(i)].append(i)

        # sort letter and place them back
        res = list(s)
        for idxs in data.values():
            letters = sorted(res[i] for i in idxs)
            for idx, ch in zip(idxs, letters):
                res[idx] = ch
        return "".join(res) 