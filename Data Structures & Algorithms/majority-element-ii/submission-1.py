class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        cnt = 1
        s = []
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                cnt += 1
            else:
                if cnt> len(nums) // 3:
                    s.append(nums[i])
                cnt = 1
        if cnt > len(nums) // 3:
            s.append(nums[-1])
        return s