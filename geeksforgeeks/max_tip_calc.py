'''
In a restaurant, two waiters, A and B, receive n orders per day, earning tips as per arrays arr[i] and brr[i]
respectively. If A takes the ith order, the tip is arr[i] rupees; if B takes it, the tip is brr[i] rupees.
To maximize total tips, they must distribute the orders such that:
A can handle at most x orders
B can handle at most y orders
Given that x + y ≥ n, all orders can be managed by either A or B. Return the maximum possible total tip after
processing all the orders.
'''
class Solution:
    def maxTip(self,n,x,y,arr,brr):
        diff_list = [(arr[i], brr[i], abs(arr[i] - brr[i])) for i in range(n)]
        diff_list.sort(key=lambda x: x[2], reverse=True)
        total_tips = 0
        a_count = 0
        b_count = 0
        for tip_A, tip_B, _ in diff_list:
            if (tip_A >= tip_B and a_count < x) or b_count >= y:
                total_tips += tip_A
                a_count += 1
            else:
                total_tips += tip_B
                b_count += 1
        return total_tips

n=12
x=11
y=7
arr=[3, 6, 5, 1, 9, 9, 3, 7, 3, 4, 6, 1]
brr=[6, 6, 1, 4, 5, 2, 5, 1, 9, 4, 9, 4]
print(Solution().maxTip(n,x,y,arr,brr))