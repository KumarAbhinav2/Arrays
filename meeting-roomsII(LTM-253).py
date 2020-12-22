"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...]
(si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
import heapq
from queue import PriorityQueue

class Solution:

    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        # heap initializations
        free_rooms = []
        # sorting the intervals by start time
        intervals.sort(key=lambda x:x[0])
        # pushing to heap
        heapq.heappush(free_rooms, intervals[0][1])
        # Iterating over the rest of the interval
        for i in intervals[1:]:
            # if the due room is free, assign the room for meeting
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            # add the new room or same room with updated time
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)

    # Time Complexity O(NlogN) - sorting O(NlogN) for n elements, worst case N*lonN min heap operations
    # Space Complexity - O(N) for min heap construction

    def minMeetingRoom_PQ(self, intervals):
        if not intervals:
            return 0
        q = PriorityQueue()
        rooms = 1
        # sorting the intervals by start time
        intervals.sort(key = lambda x:x[0])
        # adding the first interval to the queue
        q.put((intervals[0][1], intervals[0]))
        # iterating over rest of the interval
        for intv in intervals[1:]:
            val, node = q.get()
            # Check available room is free or not
            if val > intv[0]:
                rooms+=1
                q.put((val, node))
            q.put((intv[1], intv))
        return rooms