import collections
SIZE = 300
class HitCounter(object):
    def __init__(self):
        self.hit_deque = collections.deque([0]*SIZE, maxlen=SIZE)

    def hit(self, timestamp):

        if timestamp<=SIZE:
            self.hit_deque[timestamp-1] += 1
            return

        index=0
        t = timestamp%SIZE
        for i in range(t+1):
            index = i
            self.hit_deque.append(0)
        self.hit_deque[index+1] += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # if timestamp <= SIZE:
        print(obj.hit_deque)
        return sum(self.hit_deque)
        # else:
        #     t = timestamp%SIZE
        #     for i in range(t):
        #         self.hit_deque.append(0)
        #     return sum(self.hit_deque)


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
obj.hit(4)
print(obj.getHits(300))
obj.hit(302)
print(obj.getHits(303))
