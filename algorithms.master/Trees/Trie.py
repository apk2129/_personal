import collections

class TrieNode:

    def __init__(self):
        self.is_word  = False
        self.children = collections.defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        current = self.root
        for l in word:
            current = current.children[l]

        current.is_word = True

    def search(self, word):

        current = self.root
        for l in word:
            current = current.children.get(l)
            if current == None:
                return False

        return current.is_word

    def startwith(self, word):

        current = self.root
        for l in word:
            current = current.children.get(l)
            if current == None:
                return False

        return True


t = Trie()
t.insert("Anish")
t.insert("any")
print(t.startwith("an"))
