class LinkedList:

    def __init__(self, val= None, next = None):

        self.val  = val
        self.next = next

    def print_list(self):
        node = self
        r=''
        while node:
            r+= str(node.val)
            node = node.next
            if node: r += "-->"

        print(r)

    def remove_elements_greater_than_k(self, k):

        node = self
        prev = None
        while node:
            print(node.val, prev.val)
            if node.val > k:
                prev.next = node.next
            else:
                prev = node
            node = node.next

if __name__=="__main__":

    # t e s t c a s e  I
    # 1-->2-->3-->4-->5     k = 3
    l6 = LinkedList(6)
    l5 = LinkedList(5,l6)
    l4 = LinkedList(4,l5)
    l3 = LinkedList(3, l4)
    l2 = LinkedList(2,l3)
    l1 = LinkedList(1,l2)

    l1.print_list()
    l1.remove_elements_greater_than_k(3)
    l1.print_list()

    # t e s t c a s e  II
    #10-->2-->32-->4-->5  k = 5

    l1 = LinkedList(10,LinkedList(2,LinkedList(32,LinkedList(4,LinkedList(5)))))
    l1.print_list()
    l1.remove_elements_greater_than_k(5)
    l1.print_list()
