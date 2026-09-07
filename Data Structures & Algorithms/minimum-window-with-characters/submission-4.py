from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = {}
        have, required = 0, len(need)
        best_len, best = float("inf"), [-1, -1]
        left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best = [left, right]
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = best
        return s[l:r + 1] if best_len != float("inf") else ""