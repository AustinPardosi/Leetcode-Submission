class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always make sure nums1 is the smallest
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            l1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            r1 = nums1[partition1] if partition1 < m else float('inf')
            l2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            r2 = nums2[partition2] if partition2 < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2:
                    return float(max(l1, l2))
                else:
                    return (max(l1,l2) + min(r1,r2)) / 2

            elif l1 > r2:
                right = partition1 - 1

            else:
                left = partition1 + 1