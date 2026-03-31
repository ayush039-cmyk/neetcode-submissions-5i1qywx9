class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        s = []
        for i in range(k):
            maxi = max(freq , key = freq.get)
            s.append(maxi)
            del freq[maxi]
        return s