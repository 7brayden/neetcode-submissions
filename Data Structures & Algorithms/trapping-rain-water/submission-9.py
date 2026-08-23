class Solution:
    def trap(self, height: List[int]) -> int:
        leftIdx = 0
        rightIdx = len(height) - 1
        leftMax = height[leftIdx]
        rightMax = height[rightIdx]
        total = 0
        while rightIdx > leftIdx:
            if height[leftIdx] < height[rightIdx]:
                if height[leftIdx] >= leftMax:
                    leftMax = height[leftIdx]
                else:
                    increment = leftMax - height[leftIdx]
                    total += increment
                leftIdx += 1
            else:
                if height[rightIdx] >= rightMax:
                    rightMax = height[rightIdx]
                else:
                    increment = rightMax - height[rightIdx]
                    total += increment
                rightIdx -= 1
        return total
        
