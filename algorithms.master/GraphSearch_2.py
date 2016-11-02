from GraphSearch_1 import Queue
class Square_Grid:

    def __init__(self, width, height):

        self.width  = width
        self.height = height
        self.walls  = []

    def in_bounds(self, vertex):

        (x ,y) = id
        return 0 <= x < self.width and 0<= y <self.height

    def passable(self, vertex):

        return id not in self.walls

    def neighbours(self, vertex):

        (x,y) = vertex

        results = [(x+1,y), (x, y-1), (x-1,y),(x,y+1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)

        return results




def BFS(graph, start):

    frontier = Queue()
    frontier.put(start)

    came_from = {}
    came_from[start] = True

    while not frontier.empty():
        frontier.dump()
        current = frontier.get()
        for next in graph.neighbours(current):

            if next not in came_from:
                frontier.put(next)
                came_from[nex] = True



g = Square_Grid(10,10)
BFS(g, (0,0))
