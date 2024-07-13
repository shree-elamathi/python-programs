'''
There are n 1-indexed robots, each having a position on a line, health, and movement direction.
You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for
left or 'R' for right). All integers in positions are unique.
All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever
share the same position while moving, they will collide.
If two robots collide, the robot with lower health is removed from the line, and the health of the other robot
decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same
health, they are both removed from the line.
Your task is to determine the health of the robots that survive the collisions, in the same order that the robots
were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there
are no survivors, return an empty array.
Return an array containing the health of the remaining robots (in the order they were given in the input), after
no further collisions can occur.
Note: The positions may be unsorted.
'''
class Solution:
    def survivedRobotsHealths(self,positions,healths,directions):
        robots=list(zip(positions,healths,directions,range(len(positions))))
        robots.sort()
        stack=[]
        survivors=[]
        for pos,health,direction,original_ind in robots:
            if direction=="R":
                stack.append((pos,health,direction,original_ind))
            else:
                while stack and stack[-1][2]=="R":
                    r_pos,r_health,r_direction,r_ind=stack.pop()
                    if r_health>health:
                        r_health-=1
                        stack.append((r_pos,r_health,r_direction,r_ind))
                        health=0
                        break
                    elif r_health<health:
                        health-=1
                    else:
                        health=0
                        break
                if health>0:
                    survivors.append((pos,health,direction,original_ind))
        survivors += stack
        survivors.sort(key=lambda x: x[3])
        return [health for _, health, _, _ in survivors]

positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
print(Solution().survivedRobotsHealths(positions,healths,directions))
