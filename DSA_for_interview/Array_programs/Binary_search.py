'''
Alice has cards arranged in descending order and return the position of the card with minimum moves.
'''


# cards -> is the value on the cards
# query -> is the value that we should find index for

class Solution:
    # one method is to go for brute force approach where we check each value and return the pos
    def brute_locate_card(self, cards, query):
        pos = 0
        while pos < len(cards):
            if cards[pos] == query:
                return pos
            pos += 1
        return -1

    # This function is to check if there is multiple occurence and to return the first occurence index
    # If multiple occurence then return the pos of 1st occurence
    def test_location(self, cards, query, mid):
        while mid - 1 >= 0:
            if cards[mid - 1] != query:
                return mid
            mid -= 1
        return mid

    def locate_card(self, cards, query):
        # this method is for decreasing order
        left, right = 0, len(cards) - 1
        while left <= right:
            mid = (left + right) // 2  # finding the mid value for the current list
            mid_num = cards[mid]  # This represents the mid number
            if mid_num == query:
                return self.test_location(cards, query, mid)
            elif mid_num < query:
                right = mid - 1
            elif mid_num > query:
                left = mid + 1
        return -1

    # in a sorted arr to find the starting and ending index of a number
    def FindStartAndEndPos(self, nums, val):
        # this method is for sorted array
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]
            if mid_num == val:
                start_pos = self.StartPos(nums, val, mid)
                end_pos = self.EndPos(nums, val, mid)
                print(start_pos, end_pos)
                return
            elif mid_num > val:
                right = mid - 1
            elif mid_num < val:
                left = mid + 1
        return ("Not found")

    def StartPos(self, nums, val, mid):
        while mid - 1 >= 0:
            if nums[mid - 1] != val:
                return mid
            mid -= 1
        return mid

    def EndPos(self, nums, val, mid):
        while mid + 1 < len(nums):
            if nums[mid+1] != val:
                return mid
            mid += 1
        return mid


cards = [9, 9, 9, 9, 9, 9, 7, 6, 4, 3, 3, 3, 3, 3, 3, 2, 1]
query = 9
nums = [8]
val = 8
# print(Solution().locate_card(cards, query))
Solution().FindStartAndEndPos(nums, val)
