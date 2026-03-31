class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        if len(nums) == 0:
            return 0
        nums.sort()
        s = [nums[0]]
        for i in range(0,len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                s.append(nums[i])
            elif  nums[i] == nums[i+1]:
                continue
            else:
                maxi = max(len(s) , maxi)
                s = [nums[i]]
        maxi = max(len(s), maxi)

        return maxi