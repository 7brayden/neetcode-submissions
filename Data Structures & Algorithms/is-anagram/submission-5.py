class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_set = {}
        for i in range(len(s)):
            hash_set[s[i]] = hash_set.get(s[i], 0) + 1
            hash_set[t[i]] = hash_set.get(t[i], 0) - 1
        return all(v == 0 for v in hash_set.values())