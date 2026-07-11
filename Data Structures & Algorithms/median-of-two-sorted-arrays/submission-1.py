class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        l, h = 0, m
        half = (m + n + 1) // 2

        while l <= h:
            mid1 = (l + h) // 2
            mid2 = half - mid1
            left1 = float("-inf") if mid1 == 0 else nums1[mid1 - 1]
            right1 = float("inf") if mid1 == m else nums1[mid1]
            left2 = float("-inf") if mid2 == 0 else nums2[mid2 - 1]
            right2 = float("inf") if mid2 == n else nums2[mid2]
            if left1 > right2:
                h = mid1 - 1
            elif left2 > right1:
                l = mid1 + 1
            else:
                if (m + n) % 2:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2