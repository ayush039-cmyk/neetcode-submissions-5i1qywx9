class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        for i in range(0,len(nums)):
            product = 1
            for j in range(0,len(nums)):
                if j != len(nums) :
                    if j == i:
                        continue
                    else:
                        product *= nums[j]
                else:
                    break 
            prod.append(product)
        return prod
            
