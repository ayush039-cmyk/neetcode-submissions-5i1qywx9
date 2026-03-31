class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        num = len(nums) - k
        for _ in range(num):
            heapq.heappop(nums)
        return heapq.heappop(nums)