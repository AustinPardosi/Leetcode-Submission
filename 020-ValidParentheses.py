class Solution:
    def isValid(self, s: str) -> bool:
        storage = []
        pairs = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for item in s:
            if item in pairs:
                if len(storage) == 0 or storage.pop() != pairs[item]:
                    return False
            else:
                storage.append(item)
        return len(storage) == 0