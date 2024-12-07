'''
Alice has cards arranged in descending order and return the position of the card with minimum moves.
'''
# cards -> is the value on the cards
# query -> is the value that we should find index for

class Solution:
    # one method is to go for brute force approach where we check each value and return the pos
    def brute_locate_card(self,cards,query):
        pos=0
        while pos<len(cards):
            if cards[pos]==query:
                return pos
            pos+=1
        return -1

#This function is to check if there is multiple occurence and to return the first occurence index
#If multiple occurence then return the pos of 1st occurence
    def test_location(self,cards,query,mid):
        while mid-1>=0:
            if cards[mid-1]!=query:
                return mid
            mid-=1
        return mid

    def locate_card(self,cards,query):
        left,right=0,len(cards)-1
        while left<=right:
            mid=(left+right)//2 #finding the mid value for the current list
            mid_num=cards[mid] #This represents the mid number
            if mid_num==query:
                return self.test_location(cards,query,mid)
            elif mid_num<query:
                right=mid-1
            elif mid_num>query:
                left=mid+1
        return -1


cards = [9,9,9,9,9,9,7,6,4,3,3,3,3,3,3,2,1]
query = 9
print(Solution().locate_card(cards,query))
