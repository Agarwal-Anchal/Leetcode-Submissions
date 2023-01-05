class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points, key = lambda x: x[1])
        c=1
        maxi=points[0][1]
        for i,j in points:
            if i>maxi:
                maxi=j
                c+=1
        return c
