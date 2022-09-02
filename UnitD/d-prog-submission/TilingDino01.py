# CS4102 Spring 2022 -- Unit D Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: 
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################

class TilingDino:
    blackWhiteMatrix = []
    contentMatrix = []
    adjacencyMatrix = []
    numberedHashMatrix = []
    parent = []
    solution = []
    
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        # the easiest case to eliminate is the case that there is an odd number of "#"s
        # we'll also use this step to put everything into a matrix
        hashCounter = 0
        for line in lines:
            for i in line: 
                if ( i == "#" ): 
                    hashCounter+=1
        
        if ( hashCounter % 2 == 1 ): 
            return ["impossible"]

        for line in lines: 
            self.blackWhiteMatrix.append([0] * len(lines[0]))
            self.contentMatrix.append([0] * len(lines[0]))
            self.numberedHashMatrix.append([0] * len(lines[0]))

        hashCounter = 0
        for i in range(0, len(lines)):
            for j in range(0, len(lines[0])): 
                if ( lines[i][j] == "#" ): 
                    hashCounter+=1
                    self.numberedHashMatrix[i][j] = hashCounter
                

        # now lets initialize the blackWhiteMatrix and the contentMatrix
        for i in range(0, len(lines)): 
            for j in range(0, len(lines[0])): 
                self.blackWhiteMatrix[i][j] = (i + j) % 2
                self.contentMatrix[i][j] = lines[i][j]

        # now lets use create an adjacency matrix for all the nodes
        # nodes that have a blackWhite value of 0 are closer to the source
        # nodes with a blackWhite value of 1 are closer to the sink
        # the 0th node is always the source
        # the n + 1th node is always the sink

        for i in range(0, hashCounter + 2): 
            self.adjacencyMatrix.append([0] * (hashCounter + 2))

        # now lets fill in our adjacencyMatrix: 

        hashCounter2 = 0
        for i in range(0, len(lines)):
            for j in range(0, len(lines[0])): 
                if ( lines[i][j] == "#" ): 
                    hashCounter2 += 1
                    if ( self.blackWhiteMatrix[i][j] == 0 ): # we have a white node
                        self.adjacencyMatrix[0][hashCounter2] = 1 # connection between source and a "white" node
                        # lets check the adjacent spots for a valid hash and accordingly fill in the adjMatrix
                        # have to edge bounding checks
                        counter = 0
                        if ( i + 1 < len(lines) ): 
                            if ( lines[i + 1][j] == "#" ): # can't handle this case here
                                counter = 1
                                self.adjacencyMatrix[hashCounter2][self.numberedHashMatrix[i + 1][j]] = 1
                        if ( i - 1 >= 0 ): 
                            if ( lines[i - 1][j] == "#" ):
                                counter = 1 
                                self.adjacencyMatrix[hashCounter2][self.numberedHashMatrix[i - 1][j]] = 1
                        if ( j - 1 >= 0): 
                            if ( lines[i][j - 1] == "#" ): 
                                counter = 1
                                self.adjacencyMatrix[hashCounter2][hashCounter2 - 1] = 1
                        if ( j + 1 < len(lines[0]) ):
                            if ( lines[i][j + 1] == "#" ):
                                counter = 1 
                                self.adjacencyMatrix[hashCounter2][hashCounter2 + 1] = 1
                        if ( counter == 0 ): 
                            return ["impossible"]

                    else: 
                        self.adjacencyMatrix[hashCounter2][hashCounter + 1] = 1 # link from black to sink

        maxFlow = self.FordFulkerson(0, len(self.adjacencyMatrix) - 1)

        RETURNVALUE = []
        
        if (maxFlow == hashCounter/2): 
            for i in self.solution: 
                # lets first find the coordinates of hash number i[0]
                for j in range(0, len(self.numberedHashMatrix)): 
                    for k in range(0, len(self.numberedHashMatrix[0])):
                        if ( i[0] == self.numberedHashMatrix[j][k] ):
                            RETURNVALUE.append(str(k) + ' ')
                            RETURNVALUE.append(str(j) + ' ')

                        if ( i[1] == self.numberedHashMatrix[j][k] ): 
                            # RETURNVALUE.append(str(j) + ' ')
                            # RETURNVALUE.append(str(k) + ' ')
                            RETURNVALUE.append(str(k) + ' ')
                            RETURNVALUE.append(str(j) + ' ')

                RETURNVALUE.append("\n")

            s = ''.join(RETURNVALUE)
            return [s]

        return ["impossible"]

    # the corresponding code for BFS and ford-fulkerson was borrowed from geeks for geeks
    # https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(len(self.adjacencyMatrix))
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.adjacencyMatrix[u]): # maybe we need to take the transpose of the adjacency matrix? 
                if visited[ind] == False and val > 0:
                      # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # We didn't reach sink in BFS starting
        # from source, so return false
        return False

    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        self.parent = [-1]*(len(self.adjacencyMatrix))
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, self.parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.adjacencyMatrix[self.parent[s]][s])
                s = self.parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = self.parent[v]
                self.adjacencyMatrix[u][v] -= path_flow
                self.adjacencyMatrix[v][u] += path_flow
                # lets find the coordinates of u and v and push them into the solution
                if ( u != 0 and v != len(self.adjacencyMatrix) - 1):
                    self.solution.append([u, v])
                v = self.parent[v]
 
        return max_flow