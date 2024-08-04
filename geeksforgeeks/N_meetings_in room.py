'''
You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i
and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single
meeting room, when only one meeting can be held in the meeting room at a particular time.
Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
'''
class Solution:
    def maximumMeetings1(self,n,start,end):
        time=[]
        prev=None
        timing=max(end) - min(start)
        c=0
        for i in range(n):
            if prev==start[i]:
                continue
            elif end[i] in start:
                x=start.index(end[i])
                t=min(end[i]-start[i],end[x]-start[x])+1
                time.append(t)
                prev=start[x]
            else:
                t=(end[i]-start[i])+1
                time.append(t)
        time.sort()
        temp=time[0]
        for i in time:
            if temp <=timing:
                temp += i
                c+=1
            else:
                break
        return c

    def maximumMeetings(self, n, start, end):
        meetings=sorted(zip(start, end), key=lambda x: x[1])
        last_end_time=-1
        count=0
        for s,e in meetings:
            if s>last_end_time:
                count+=1
                last_end_time=e
        return count
n=4
start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
end = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
print(Solution().maximumMeetings(n,start,end))
print(Solution().maximumMeetings1(n,start,end))
