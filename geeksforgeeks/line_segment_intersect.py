'''
Given the coordinates of the endpoints(p1,q1, and p2,q2) of the two line segments. Check if they intersect or
not. If the Line segments intersect return true otherwise return false.
Note: Please check the intersection lies within the line segments.
'''
class Solution:
    def doIntersect(self, p1, q1, p2, q2):
        def on_segment(p, q, r):
            return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val==0:
                return 0
            return 1 if val > 0 else 2
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)
        if (o1 != o2 and o3 != o4):
            return "true"
        if (o1 == 0 and on_segment(p1, p2, q1)):
            return "true"
        if (o2 == 0 and on_segment(p1, q2, q1)):
            return "true"
        if (o3 == 0 and on_segment(p2, p1, q2)):
            return "true"
        if (o4 == 0 and on_segment(p2, q1, q2)):
            return "true"
        return "false"
p1=(1,1)
q1=(10,1)
p2=(1,2)
q2=(10,2)
print(Solution().doIntersect(p1,q1,p2,q2))
