class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            so = ''.join(sorted(s))
            res[so].append(s)
        return list(res.values())