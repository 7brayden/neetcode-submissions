class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left = 0
        right = (len(heights) - 1)
        while right > left:
            if heights[left] > heights[right]:
                area = abs(left - right) * heights[right]
                if area > best:
                    best = area
                right -= 1
            else:
                area = abs(left - right) * heights[left]
                if area > best:
                    best = area
                left += 1
        return best