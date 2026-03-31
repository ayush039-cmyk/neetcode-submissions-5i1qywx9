class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for p,q in points:
            res.append((p*p+q*q , [p,q]))

        heapq.heapify(res)
        result = []
        for _ in range(k):
            distance , point = heapq.heappop(res)
            result.append(point)

        return result