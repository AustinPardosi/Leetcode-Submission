class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                water += (maxLeft - height[l])
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                water += (maxRight - height[r])
        return water
            