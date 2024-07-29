'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
You have to form a team of 3 soldiers amongst them under the following rules:
Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where
(0 <= i < j < k < n). Return the number of teams you can form given the conditions. (soldiers can be part of
multiple teams).
'''
class Solution:
    def numTeams(self, rating):
        n=len(rating)
        teams=0
        for j in range(n):
            less_left=more_left=0
            less_right=more_right=0
            for i in range(j):
                if rating[i]<rating[j]:
                    less_left+=1
                if rating[i]>rating[j]:
                    more_left+=1
            for k in range(j+1,n):
                if rating[k]<rating[j]:
                    less_right+=1
                if rating[k]>rating[j]:
                    more_right+=1
            teams+=less_left*more_right+less_right*more_left
        return teams

rating=[2,5,3,4,1]
print(Solution().numTeams(rating))