class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cnt =1
        n = len(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                if cnt> n/2:
                    return nums[i-1]
                cnt = 1
        if cnt > n/2:
            return nums[-1]

        return -1
            