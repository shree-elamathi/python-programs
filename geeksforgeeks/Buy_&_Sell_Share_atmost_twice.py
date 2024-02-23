#In daily share trading, a buyer buys shares in the morning and sells them on the same day.
# If the trader is allowed to make at most 2 transactions in a day, the second transaction can
# only start after the first one is complete (buy->sell->buy->sell). The stock prices throughout
# the day are represented in the form of an array of prices.
# Given an array price of size n, find out the maximum profit that a share trader could have made.
class solution:
    def maxProfit(self,n,price):
        fbuy,fsell=-99999,0
        sbuy,ssell=-99999,0
        for i in price:
            fbuy=max(fbuy,-i)
            fsell=max(fsell,i+fbuy)
            sbuy=max(sbuy,fsell-i)
            ssell=max(ssell,sbuy+i)
        return ssell

n=5
price=[1,2,1,2]
print(solution().maxProfit(n,price))
