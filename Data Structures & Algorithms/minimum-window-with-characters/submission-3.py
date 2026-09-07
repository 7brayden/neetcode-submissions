class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        shorter_dict = {}
        window = {}
        left = 0
        best_left = 0
        best_len = float("inf")
        for char in t:
            if char not in shorter_dict:
                shorter_dict[char] = 1
            else:
                shorter_dict[char] += 1
        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            flag = True
            for i in shorter_dict:
                if shorter_dict[i] > window.get(i,0):
                    flag = False
                    break
            while flag:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                window[s[left]] -= 1
                left += 1
                
                flag = True 
                for i in shorter_dict:
                    if shorter_dict[i] > window.get(i,0):
                        flag = False
                        break
        return "" if best_len == float("inf") else s[best_left : best_left + best_len]

                

        