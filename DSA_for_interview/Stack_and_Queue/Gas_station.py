'''
There are some gas stations along a circular route. You are given two integer arrays gas[] denoted as the amount of
gas present at each station and cost[] denoted as the cost of travelling to the next station. You have a car with an
unlimited gas tank. You begin the journey with an empty tank from one of the gas stations. Return the index of the
starting gas station if it's possible to travel around the circuit without running out of gas at any station in a
clockwise direction. If there is no such starting station exists, return -1.
Note: If a solution exists, it is guaranteed to be unique.
'''

class Solution:
    def startStation(self, gas, cost):
        strtInd = 0
        curgas = 0
        for i in range(len(gas)):
            curgas = curgas + gas[i] - cost[i]
            if curgas < 0:
                strtInd = i + 1
                curgas = 0
        curgas = 0
        for i in range(len(gas)):
            indx = (i + strtInd) % len(gas)
            curgas = curgas + gas[indx] - cost[indx]
            if curgas < 0:
                return -1
        return strtInd

gas = [4, 5, 7, 4]
cost = [6, 6, 3, 5]
print(Solution().startStation(gas,cost))