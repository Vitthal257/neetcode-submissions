class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,num1
        m,n = len(nums1), len(nums2)
        l = 0
        h = m
        half = (m+n)//2
        while l<=m:
            mid1 = (l+m)//2
            mid2 = half-mid1
            left1 = nums1[mid1-1]
            right1 = nums1[mid1]
            left2 = nums2[mid2-1]
            right2 = nums2[mid2]
            