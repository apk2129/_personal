import collections

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_word  = False
        self.children = collections.defaultdict(TrieNode)


d = TrieNode()

print(d.children[3].children == None)
print(d.children.get(3) == {})
