import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Minimum possible speed is 1 banana per hour.
        left = 1

        # Maximum possible speed is the largest pile.
        # At this speed, Koko can finish each pile in 1 hour.
        right = max(piles)

        # Keep searching while there are possible speeds to check.
        while left < right:
            # Test the speed in the middle of our search range.
            k = (left + right) // 2

            # Calculate how many hours Koko needs at speed k.
            hours = 0

            for pile in piles:
                # Calculate the hours needed for this individual pile.
                # Integer ceiling division: ceil(pile / k)
                hours += (pile + k - 1) // k

            # If Koko can finish within h hours, this speed works.
            if hours <= h:
                # Try a smaller speed to find the minimum.
                # Keep k because it might be the answer.
                right = k
            else:
                # This speed is too slow, so try a higher speed.
                # k cannot be the answer.
                left = k + 1

        # left and right meet at the minimum speed that works.
        return left