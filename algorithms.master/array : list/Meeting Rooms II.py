
''' ----------------------------------------------------------------------------------------------------------------------------------------
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
