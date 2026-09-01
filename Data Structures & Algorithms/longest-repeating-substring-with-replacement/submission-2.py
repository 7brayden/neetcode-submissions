class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        best = 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            windowLength = right - left + 1
            if windowLength - (k + max(count.values())) > 0:
                count[s[left]] -= 1
                left += 1
                windowLength = right - left + 1
            if windowLength > best:
                best = windowLength
        return best 
                

            
