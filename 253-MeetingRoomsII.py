# Brute Force
# Time: O(n^2) — for each meeting's start time, check every meeting
# Space: O(1) — only use a few variables
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        result = 0

        # Check each meeting's start time to find the maximum overlap
        for start, end in intervals:
            count = 0

            # Count how many meetings are active at this start time
            for meetingStart, meetingEnd in intervals:
                if meetingStart <= start < meetingEnd:
                    count += 1

            # Keep the maximum number of simultaneous meetings
            result = max(count, result)

        return result


# Priority Queue (Min Heap)
import heapq

# Time: O(n log n) — sorting and heap operations for each meeting
# Space: O(n) — the heap can store up to n meeting end times
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # Sort meetings by start time so we process them chronologically
        intervals.sort(key=lambda meeting: meeting[0])

        # Store the end times of meetings occupying rooms
        rooms = []
        result = 0

        for start, end in intervals:
            # Free rooms whose meetings have ended before or when this starts
            while rooms and start >= rooms[0]:
                heapq.heappop(rooms)

            # Assign a room to the current meeting by storing its end time
            heapq.heappush(rooms, end)

            # Track the maximum number of rooms needed simultaneously
            result = max(len(rooms), result)

        return result