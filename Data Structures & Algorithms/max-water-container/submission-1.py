class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 1
        max_volume = 0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                m = min(heights[i],heights[j])
                volume = m * (j-i)
                max_volume = max(volume,max_volume)
        return max_volume
