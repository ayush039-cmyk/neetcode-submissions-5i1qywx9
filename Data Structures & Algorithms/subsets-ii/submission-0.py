class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,op):
            if i == len(nums):
                res.append(op.copy())
                return 

            op.append(nums[i])
            dfs(i+1,op)
            op.pop()
            

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1,op)

        dfs(0,[])
        return res