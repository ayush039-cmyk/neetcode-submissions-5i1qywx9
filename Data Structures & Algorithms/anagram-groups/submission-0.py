class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorteda = ''.join(sorted(s))
            res[sorteda].append(s)
        return list(res.values())