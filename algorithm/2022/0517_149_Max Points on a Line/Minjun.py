# 통과못한 풀이
# 한 점에서 모든 점에 대한 기울기를 구하고자 합니다
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        gx = []
        gy = []
        gxy = []
        
        for i in range(len(points)-1):
            dx = points[i+1][0] - points[i][0]
            dy = points[i+1][1] - points[i][1]
            gx.append(dx)
            gy.append(dy)
        for i in range(len(str(dx))):
            g = gy[i] / gx[i]
            gxy.append([g])
        print(gx,gy,gxy)
