'''
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three
possible types of commands:
-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs
into an obstacle, then it will instead stay in its current location and move on to the next command.
Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5,
return 25).
Note:
North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
There can be obstacle in [0,0].

Naive Approach

class Solution:
    def robotSim(self,commands,obstacles):
        dict={"north":0,"west":1,"south":2,"east":3}
        directions=[["west","east"],["south","north"],["west","east"],["north","south"]]
        current_dir="north"
        cur_point=[0,0]
        x=cur_point[0]
        y=cur_point[1]
        for i in commands:
            if i==-1:
                ind=dict.get(current_dir)
                lst=directions[ind]
                current_dir=lst[1]
            elif i==-2:
                ind=dict.get(current_dir)
                lst = directions[ind]
                current_dir = lst[0]
            else:
                if current_dir=="north":
                    cur_point=self.North(cur_point,i,obstacles)
                    print(cur_point)
                elif current_dir=="west":
                    cur_point=self.West(cur_point,i,obstacles)
                    print(cur_point)
                elif current_dir=="east":
                    cur_point=self.East(cur_point,i,obstacles)
                    print(cur_point)
                else:
                    cur_point=self.South(cur_point,i,obstacles)
                    print(cur_point)
                if x<=abs(cur_point[0]) and y<=abs(cur_point[1]):
                    x=cur_point[0]
                    y=cur_point[1]
        x=x*x
        y=y*y
        return x+y

    def North(self,cur_point,val,obstacles):
        x=cur_point[0]
        for i in range(val):
            y=cur_point[1]+1
            if [x,y] in obstacles:
                return cur_point
            else:
                cur_point[1]+=1
        return cur_point

    def West(self,cur_point,val,obstacles):
        y = cur_point[1]
        for i in range(val):
            x = cur_point[0] - 1
            if [x, y] in obstacles:
                return cur_point
            else:
                cur_point[0] -= 1
        return cur_point
    def East(self,cur_point,val,obstacles):
        y = cur_point[1]
        for i in range(val):
            x = cur_point[0] + 1
            if [x, y] in obstacles:
                return cur_point
            else:
                cur_point[0] += 1
        return cur_point
    def South(self,cur_point,val,obstacles):
        x = cur_point[0]
        for i in range(val):
            y = cur_point[1] - 1
            if [x, y] in obstacles:
                return cur_point
            else:
                cur_point[1] -= 1
        return cur_point
'''
class Solution:
    def robotSim(self,commands,obstacles):
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        direction_ind=0
        x,y=0,0
        max_dist=0
        obstacle_set = set(map(tuple, obstacles))
        for command in commands:
            if command==-1:
                direction_ind=(direction_ind+1)%4
            elif command==-2:
                direction_ind=(direction_ind-1)%4
            else:
                dx,dy=directions[direction_ind]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_dist = max(max_dist, x * x + y * y)
        return max_dist

commands = [-2,8,3,7,-1]
obstacles = [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]
print(Solution().robotSim(commands,obstacles))