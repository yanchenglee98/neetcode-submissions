class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            s1 = "".join(sorted(s))
            hm[s1].append(s)
        return list(hm.values())
        