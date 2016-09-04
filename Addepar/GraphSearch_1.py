import collections


class simple_graph:

    def __init__(self):
        self.edges = {}

    def neighbours(self, vertex):
        return self.edges[vertex]


class Queue:

    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements)==0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

    def dump(self):
        print(self.elements)

def BFS(graph, start, goal=None):

    frontier = Queue()
    frontier.put(start)

    visited = {}
    visited[start] = True

    while not frontier.empty():
        frontier.dump()
        #1 pop from queuee
        current = frontier.get()
        print("Visiting " + current)

        if current == goal:
            break
        for next in graph.neighbours(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
        print("------------------")


if __name__=="__main__":

    g = simple_graph()
    g.edges = {
        'A' : ['B'],
        'B' : ['A', 'C', 'D'],
        'C' : ['A'],
        'D' : ['E', 'A'],
        'E' : ['B']
    }

    BFS(g, 'A') #without target
    print("\n\n\n")
    BFS(g, 'A' , 'C') #with target
