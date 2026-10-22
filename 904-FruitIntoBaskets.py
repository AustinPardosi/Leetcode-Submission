from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l = 0
        count = defaultdict(int) # Type : Count
        result = 0

        for r in range(len(fruits)):
            # 1. Expand: pick the fruit at tree r
            count[fruits[r]] += 1

            # 2. Shrink: more than 2 types means we need a 3rd basket,
            #    so drop fruit from the left until only 2 types remain
            while len(count) > 2:
                count[fruits[l]] -= 1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                
                l += 1
            
            # 3. Window has at most 2 types, record its size
            result = max((r - l + 1), result)

        return result

