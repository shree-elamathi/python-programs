'''
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a
triple booking.
A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the
three events.).
The event can be represented as a pair of integers start and end that represents a booking on the half-open interval
[start, end), the range of real numbers x such that start <= x < end.
Implement the MyCalendarTwo class:
MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing
a triple booking. Otherwise, return false and do not add the event to the calendar.
'''


class MyCalendarTwo:

    def __init__(self):
        # A list to store all events
        self.events = []
        # A list to store overlapping intervals (double bookings)
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new event would cause a triple booking
        for o_start, o_end in self.overlaps:
            # If there's an overlap with a double-booked interval, return False
            if max(start, o_start) < min(end, o_end):
                return False

        # Check for overlaps with existing events
        for e_start, e_end in self.events:
            # Find the overlap between the current event and the new one
            if max(start, e_start) < min(end, e_end):
                # If they overlap, add the overlap to the overlaps list
                self.overlaps.append((max(start, e_start), min(end, e_end)))

        # Add the new event to the events list
        self.events.append((start, end))
        return True
