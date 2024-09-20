class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        start_idx = 0
        final_idx = len(height) - 1

        while start_idx != final_idx:
            width = final_idx - start_idx
            standard_height = min(height[start_idx], height[final_idx])
            area = max(area, width * standard_height)

            if height[start_idx] < height[final_idx]:
                start_idx += 1
            else:
                final_idx -= 1

        return area