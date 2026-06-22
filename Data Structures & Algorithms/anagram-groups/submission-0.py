from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for items in strs:
            key = "".join(sorted(items))
            mp[key].append(items)
        return list(mp.values())


