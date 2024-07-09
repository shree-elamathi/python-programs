'''
There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:
arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer
waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a
time. The chef prepares food for customers in the order they were given in the input.
Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered
accepted.
'''
class Solution:
    def averageWaaitingTime(self,customers):
        prev_completion_time=0
        waiting_time=[]
        for i in customers:
            if prev_completion_time==0 or prev_completion_time<i[0]:
                prev_completion_time=i[0]
            complete_time=prev_completion_time+i[1]
            prev_completion_time=complete_time
            waiting_time.append(complete_time-i[0])
        avg=sum(waiting_time)/len(waiting_time)
        return round(avg,5)

customers=[[5,2],[5,4],[10,3],[20,1]]
print(Solution().averageWaaitingTime(customers))