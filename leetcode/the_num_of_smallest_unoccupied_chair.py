'''
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in
this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair
with the smallest number.
For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at
that same moment, they can sit in that chair.
You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and
leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.
Return the chair number that the friend numbered targetFriend will sit on.
'''
import heapq
class Solution:
    def smallestChair(self, times, targetFriend):
        n = len(times)
        events = []
        for i in range(n):
            arrival, leaving = times[i]
            events.append((arrival, i, 'arrive'))
            events.append((leaving, i, 'leave'))
        events.sort(key=lambda x: (x[0], x[2] == 'arrive'))
        available_chairs = []
        occupied_chairs = []
        for i in range(n):
            heapq.heappush(available_chairs, i)
        friend_to_chair = {}
        for time, friend, event_type in events:
            if event_type == 'arrive':
                chair = heapq.heappop(available_chairs)
                friend_to_chair[friend] = chair
                if friend == targetFriend:
                    return chair
            else:
                chair = friend_to_chair[friend]
                heapq.heappush(available_chairs, chair)


times = [[1,4],[2,3],[4,6]]
targetFriend = 1
print(Solution().smallestChair(times,targetFriend))