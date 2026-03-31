class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            h = len(nums) - 1

            while l < h:
                total = nums[i] + nums[l] + nums[h]
                if total == 0:
                    s.append([nums[i], nums[l], nums[h]])
                    while l < h and nums[l] == nums[l+1]:
                        l += 1
                    while l < h and nums[h] == nums[h-1]:
                        h -= 1
                    l += 1  # ✅ move once after skipping duplicates
                    h -= 1  # ✅ move once after skipping duplicates
                elif total > 0:
                    h -= 1
                else:
                    l += 1
        return s