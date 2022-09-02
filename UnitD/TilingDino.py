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

import networkx as nx

class TilingDino:
    blackWhiteMatrix = []
    
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
            self.blackWhiteMatrix.append([0] * len(lines[0]))
            for i in line: 
                if ( i == "#" ): 
                    hashCounter+=1
        
        if ( hashCounter % 2 == 1 ): 
            return ["impossible"]            

        # now lets initialize the blackWhiteMatrix and the contentMatrix
        for i in range(0, len(lines)): 
            for j in range(0, len(lines[0])): 
                self.blackWhiteMatrix[i][j] = (i + j) % 2

        # nodes that have a blackWhite value of 0 are closer to the source
        # nodes with a blackWhite value of 1 are closer to the sink
        G = nx.DiGraph() 

        for i in range(0, len(lines)):
            for j in range(0, len(lines[0])): 
                if ( lines[i][j] == "#" ): 
                    if ( self.blackWhiteMatrix[i][j] == 0 ): # we have a white node 
                        G.add_edge("source", str(j) + " " + str(i) + " ", capacity = 1.0)

                        if ( i + 1 < len(lines) ): 
                            if ( lines[i + 1][j] == "#" ): 
                                G.add_edge(str(j) + " " + str(i) + " ", str(j) + " " + str(i + 1) + " ", capacity = 1.0)
                        
                        if ( i - 1 >= 0 ): 
                            if ( lines[i - 1][j] == "#" ):
                                G.add_edge(str(j) + " " + str(i) + " ", str(j) + " " + str(i - 1) + " ", capacity = 1.0)
                        
                        if ( j - 1 >= 0): 
                            if ( lines[i][j - 1] == "#" ): 
                                G.add_edge(str(j) + " " + str(i) + " ", str(j - 1) + " " + str(i) + " ", capacity = 1.0)
                        
                        if ( j + 1 < len(lines[0]) ):
                            if ( lines[i][j + 1] == "#" ):
                                G.add_edge(str(j) + " " + str(i) + " ", str(j + 1) + " " + str(i) + " ", capacity = 1.0)

                    else: 
                        G.add_edge(str(j) + " " + str(i) + " ", "sink", capacity = 1.0) # link from black to sink

        flow_value, flow_dict = nx.maximum_flow(G, "source", "sink")

        if flow_value * 2 != hashCounter: 
            return ["impossible"]

        solutionList = []
        RETURNVALUE = []

        for key in flow_dict["source"]:
            if flow_dict["source"][key] == 1.0: 
                solutionList.append(key)

        for key in solutionList: 
            for key1 in flow_dict[key]: 
                if flow_dict[key][key1] == 1.0: 
                    RETURNVALUE.append(key1 + key)
                    RETURNVALUE.append("\n")
    
        s = ''.join(RETURNVALUE)
        return[s]