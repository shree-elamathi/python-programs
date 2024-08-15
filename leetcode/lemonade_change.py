'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a
time(in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20
bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every
customer with the correct change, or false otherwise.
'''
class Solution:
    def lemonadeChange(self,bills):
        f_change=0
        t_change=0
        if bills[0]!=5:
            return False
        for i in bills:
            if i==5:
                f_change+=1
            elif i==10:
                if f_change<1:
                    return False
                f_change-=1
                t_change+=1
            else:
                if t_change<1:
                    if f_change<3:
                        return False
                    else:
                        f_change-=3
                else:
                    if f_change<1:
                        return False
                    t_change-=1
                    f_change-=1
        return True
bills =[5,5,5,10,20]
print(Solution().lemonadeChange(bills))
