'''
Given a circular sheet of radius, r. Find the total number of rectangles with integral length and width that
can be cut from the sheet that can fit on the circle, one at a time.
'''
class Solution:
    def rectanglesInCircle(self,r):
        rectangles=0
        diameter=2*r
        diasqr=diameter*diameter
        for a in range(1,2*r):
            for b in range(1,2*r):
                diagonallengthsquare=(a*a)+(b*b)

                if diagonallengthsquare<=diasqr:
                    rectangles+=1
        return rectangles
r=2
print(Solution().rectanglesInCircle(r))