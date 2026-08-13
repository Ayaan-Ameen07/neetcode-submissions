class Solution:
    def maxArea(self, heights: List[int]) -> int:
       l = 0
       r = len(heights)-1
       area = 0
       maxarea = 0

       while l < r:
        distance = (r- l)
        height = min(heights[l] , heights[r])
        area = distance * height
        maxarea = max(maxarea, area)
        

        if heights[l] > heights[r]:
            r-=1
        else:
            l +=1 
       return maxarea
