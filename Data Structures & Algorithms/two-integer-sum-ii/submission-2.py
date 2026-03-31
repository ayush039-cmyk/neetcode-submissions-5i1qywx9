class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) -1
        s = []
        while l<h:
            if numbers[l] + numbers[h] == target:
                s.append(l+1)
                s.append(h+1)
                return s
            if numbers[l] + numbers[h] > target:
                h -= 1
            if numbers[l] + numbers[h] < target:
                l += 1
            
        return s