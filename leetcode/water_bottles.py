'''
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty
water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
'''
class Solution:
    def numWaterBottles(self,numBottles,numExchange):
        ans=numBottles
        while numBottles>=numExchange:
            exchange=numBottles//numExchange
            ans+=exchange
            remaining=numBottles%numExchange
            numBottles=remaining+exchange
        return ans


numBottles=15
numExchange=4
print(Solution().numWaterBottles(numBottles,numExchange))