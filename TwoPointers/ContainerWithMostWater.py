'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            hgth = min(height[left_pointer],height[right_pointer])
            area = width * hgth
            maxArea = max(maxArea, area)
            
            if height[right_pointer] > height[left_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return maxArea
        