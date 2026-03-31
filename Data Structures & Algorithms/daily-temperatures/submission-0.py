class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        cnt = 0
        for i in range(0,len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:        
                    cnt = j-i
                    break
            stack.append(cnt)
            cnt = 0
        return stack
            