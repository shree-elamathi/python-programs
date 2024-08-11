'''
Given a set of n jobs where each jobi has a deadline and profit associated with it.
Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated
with a job if and only if the job is completed by its deadline.
Find the number of jobs done and the maximum profit.
Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job. Deadline of the job is the
time on or before which job needs to be completed to earn the profit.
'''
class Solution:
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x:x[2],reverse=True)
        max_deadline=max(job[1] for job in Jobs)
        slots=[-1]*(max_deadline+1)
        job_count=0
        max_profit=0
        for job in Jobs:
            job_id,deadline,profit=job
            for i in range(deadline,0,-1):
                if slots[i]==-1:
                    slots[i]=job_id
                    job_count+=1
                    max_profit+=profit
                    break
        return job_count,max_profit
Jobs = [[1,4,20],[2,1,1],[3,1,40],[4,1,30]]
print(Solution().JobScheduling(Jobs,n=4))