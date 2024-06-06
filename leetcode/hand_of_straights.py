'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of
size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
return true if she can rearrange the cards, or false otherwise.
'''
class Solution:
    def instraighthand(self,hand,groupsize):
        if len(hand)%groupsize!=0:
            return False
        hand=sorted(hand)
        for i in range(int(len(hand)/groupsize)):
            print("next loop")
            cur_val=hand[0]
            for j in range(groupsize-1):
                if cur_val+1 not in hand:
                    return False
                hand.pop(hand.index(cur_val))
                cur_val=cur_val+1
            hand.pop(hand.index(cur_val))
        return True
hand=[1,2,3,4,5]
groupsize=4
print(Solution().instraighthand(hand,groupsize))
