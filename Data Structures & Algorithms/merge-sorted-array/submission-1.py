class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = 0
        b = len(nums1) - 1
        for i in range(n):
            nums1[b] = nums2[a]
            a += 1
            b -= 1
        nums1.sort()
        return nums1