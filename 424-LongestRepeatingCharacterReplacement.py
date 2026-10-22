# Brute Force
# Time Complexity = O(n^2)
# Space Complexity = O(1)
class SolutionBruteForce:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0

        for i in range(len(s)):                 # start of substring
            count = defaultdict(int)            # letter -> count in s[i..j]
            max_count = 0                       # most frequent letter in s[i..j]

            for j in range(i, len(s)):          # end of substring
                count[s[j]] += 1
                max_count = max(max_count, count[s[j]])

                window_len = j - i + 1
                if window_len - max_count <= k:
                    best = max(best, window_len)
                else:
                    # Once a window is invalid, making it longer can't fix it:
                    # length grows by 1, max_count grows by at most 1.
                    # This is the exact property sliding window relies on.
                    break

        return best

# Sliding Window
# Time Complexity = O(26 * n) = O(n)
# Space Complexity = O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        data = defaultdict(int)   # letter -> count inside window s[l..r]
        best = 0

        for r in range(len(s)):
            # 1. Expand: bring s[r] into the window
            data[s[r]] += 1

            # 2. Shrink: while the window needs more than k replacements,
            #    remove the leftmost letter first, then move l forward
            while (r - l + 1) - max(data.values()) > k:
                data[s[l]] -= 1
                l += 1

            # 3. Window s[l..r] is valid, record its length
            best = max(best, r - l + 1)

        return best
