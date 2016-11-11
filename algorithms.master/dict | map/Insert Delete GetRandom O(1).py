class RandomizedSet(object):

    def __init__(self):

        self.nums = []
        self.pos  = {}

    def insert(self, val):

        if val not in self.nums:
            self.nums.append(val)               # append at the end
            self.pos[val] = len(self.nums) - 1  # i = len - 1 , store in map
            return True
        else:
            return False

    def remove(self, val):

        if val in self.nums:

            val_index    = self.pos[val]
            last_element = self.nums[len(self.nums)-1]

            self.nums[val_index] = last_element  #1 copy last element to val index
            self.pos[last_element] = val_index   #2 update last elemnent position in map
            self.nums.pop()                      #3 remove last element from the END

            return True
        else:
            return False


    def getRandom(self):

        random_index = random.randint(0, len(self.nums)-1 )
        return self.nums[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
