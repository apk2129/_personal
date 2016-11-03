'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

'''
def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # o b j e c t --> s o r t   l i k e   t h i s!!
        intervals.sort(key=lambda x: x.start)

        for i in range(1,len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True

'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
for example, we have meetings that span along time as follows:

|_____|
      |______|
|________|
        |_______|
Then, the start time array and end time array after sorting appear like follows:

||    ||
     |   |   |  |
'''
def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0

        start_times = sorted([i.start for i in intervals])
        end_times   = sorted([i.end   for i in intervals])

        rooms = 0
        i     = 0

        for start in start_times:
            if start<end_times[i]:
                rooms += 1
            else:
                i += 1

        return rooms
