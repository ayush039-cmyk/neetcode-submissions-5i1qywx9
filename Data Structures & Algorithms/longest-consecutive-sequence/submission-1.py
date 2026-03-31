class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = sorted(nums)
        cnt = 1
        maxi = 1
        for i in range(1,len(nums)):
            if n[i-1] + 1 == n[i]:
                cnt += 1
                maxi = max(maxi,cnt)
            elif n[i-1] == n[i]:
                continue
            else:
                maxi = max(maxi,cnt)
                cnt = 1
        return maxi