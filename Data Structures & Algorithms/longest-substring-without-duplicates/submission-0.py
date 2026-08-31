class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringWindow = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in stringWindow and stringWindow[s[right]] >= left:
                left = stringWindow[s[right]] + 1
            stringWindow[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len