class Node:

    def __init__( self, key, val ):

        self.value = val
        self.key   = key
        self.prev  = None
        self.next  = None



class LRU:

    def __init__( self, cap ):

        self.capacity  = cap
        self.cache_map = {}

        self.start_node = None
        self.tail_node = None


    def put( self, key, val ):

        # create node
        node = Node(key, val)

        if len(self.cache_map) == self.capacity:
            #capacity full --> remove tail
            self.tail_node = self.tail_node
            self.tail_node.next = None

        # insert at head
        if len(self.cache_map) == 0:
            self.start_node = node
        else:
            node.prev = None
            node.next = self.start_node
            self.start_node = node

        self.cache_map[val] = node



    def print_state ( self ):

        print(sorted(self.cache_map.keys()))



if __name__=="__main__":

    lru_C = LRU(3)
    lru_C.put(1,11)
    lru_C.put(2,22)
    lru_C.put(3,33)

    lru_C.print_state()

    lru_C.put(4,44)

    lru_C.print_state()
