class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, curr, tt):
            if tt == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or tt > target:
                return

            curr.append(nums[i])
            dfs(i+1, curr, tt+nums[i])
            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1, curr, tt)

        dfs(0, [], 0)
        return res