class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        i = defaultdict(int)
        o = defaultdict(int)

        for src , dst in trust:
            o[src] += 1
            i[dst] += 1

        for inc in range(1,n+1):
            if o[inc] == 0 and i[inc] == n-1:
                return inc

        return -1