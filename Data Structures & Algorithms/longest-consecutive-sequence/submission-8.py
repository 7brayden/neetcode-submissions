class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 1
        best_res = 0
        for n in num_set:
            if n - 1 not in num_set:
                while True:
                    if n + 1 not in num_set:
                        if longest > best_res:
                            best_res = longest
                        longest = 1
                        break
                    longest += 1
                    n += 1
        return best_res
        