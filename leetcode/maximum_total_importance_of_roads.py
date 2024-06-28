'''
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n-1.
You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a
bidirectional road connecting cities ai and bi.
You need to assign each city with an integer value from 1 to n, where each value can only be used once. The
importance of a road is then defined as the sum of the values of the two cities it connects.
Return the maximum total importance of all roads possible after assigning the values optimally.
'''
class Solution:
    def maximumImportance(self,n ,roads):
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)
        values = [0] * n
        for i in range(n):
            values[sorted_cities[i]] = n - i
        total_importance = 0
        for road in roads:
            total_importance += values[road[0]] + values[road[1]]
        return total_importance
n=9
roads=[[6,2],[2,7],[8,1],[3,7],[6,0],[5,1],[4,2],[8,3],[6,4],[5,3],[6,7],[6,8],[3,1],[4,8],[0,7],[6,1],
       [4,0],[4,3],[7,4],[5,2],[5,4],[1,7],[3,6],[8,5]]
print(Solution().maximumImportance(n,roads))