class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarr = sorted(nums1+nums2)

        n = len(newarr)

        if n % 2 != 0:
            return float(newarr[(n//2)])
        else:
            return float((newarr[(n//2)]+newarr[(n//2)-1])/2)