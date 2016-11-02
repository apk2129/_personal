                    'http://www.redblobgames.com/pathfinding/a-star/introduction.html'
                                            ------------
                                           \ G R A P H S \
                                            ------------
                                                  |
                                                  |
  ---------------------------------------------------------------------------------------------------------
  |                                  |                                      |                             |
' BFS                                DJIJAKTRAS                             GREEDY BEST FIRST SEARCH      A*
# With Breadth First Search and Dijkstra’s Algorithm,                                                     Dijkstra’s Algorithm calculates the distance from the start point.
# the frontier expands in all directions. This is a                                                       Greedy Best-First Search estimates the distance to the goal point.
# reasonable choice if you’re trying to find a path to                                                    A* is using the sum of those two distances.
# all locations or to many locations.                                                                     A* is the best of both world
# However, a common case is to find a path to only one location.
# Let’s make the frontier expand towards the goal more
# than it expands in other directions.

Explores equally in                Instead of exploring all
all directions.                    possible paths equally,
                                   it favors lower cost paths


-----------------------------------------------------------------------------------------------------------------
   L E C T U R E 9.1
------------------------------------------------------------------------------------------------------------------
<> REPRESENTATION OF GRAPHS <>

\vetices
nodes       \edges
'< n > --------m------- < n >
              / \
      *directed  *undirected
      *ordered


------------------------------------------------------------------------------------------------------------------
    L E C T U R E 9.2
------------------------------------------------------------------------------------------------------------------

<> Q >> UNIDIRECTED GRAPH ,CONNNECTED,  N VERTICES , NO PARALLELS ( LINE JOINING SAME POINTS )
<> A >> MIN ( EDGES ) = N - 1
        MAX ( EDGES ) = SUMATION(N)

\SPARSE VS DENSE
VETICES = n
EDGES   = m


<> SPARSE :  m is 0(n) ; close to lower bound | linear
<> DENSE  :  m is o(n2); close to upper bound | quadratic


\REPRESENTATION

<> ADJACENCY MATRIX  : A    {SPACE : O(n2)}
   Aij = 1 : 'if there is an edge between i and j'

<> ADJACENCY LIST :  { SPACE : O(m + n) linear space of size of graph   }
                'list of all edges of which it is a member ( directed : store on _TO_/_FROM_ vetices)
                /
    * list of vertices
    * list of edges
                \
                # 'each edge will have 2 pointers to/from edge

    # adj list is perfect for graph search

------------------------------------------------------------------------------------------------------------------
L E C T U R E 9.3
------------------------------------------------------------------------------------------------------------------

\ MINIMUM CUT PROBLEM
    --> graph partitioning (applications)
        - physical network : identify weakness in network
        - community detections
        - image segmentation ( input 2d array )

        def random contraction algorithm: sometimes identifies!
        '''
            - start with any edge
            - merge 2 vertex of that edge
            - continue till number of vertex = 2
            - once vertex = 2 , return
            - that edge is the 'minimum cut' edge of the graph
            ** random hai toh barabar nahi select hua toh minimum nahi milega hamesha

            ** useful ?? --> probablity of success ? -->
        '''
