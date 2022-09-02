# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: ssb3vk
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################

# from modulefinder import STORE_OPS
# from operator import itemgetter
# from asyncio.windows_events import NULL
# from queue import PriorityQueue
import string

class Supply:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        edgeWeightSum = 0

        # print(file_data)

        [nodeNumber, edgeNumber] = [ int(file_data[0].split()[0]), int(file_data[0].split()[1]) ]

        disjointsets = {}

        # Rules for what node can connect to what: 
        #     Pretty sure that there is only one port and this port can only connect to rail hubs or distribution current_process

        #     RailHub: Can go to other railHubs or to Distribution centers but not to stores (also not backwards to ports)

        #     Distribution center: only can go from dist center to STORE_OPS

        #     Store: Can only go to other stores and can only belong to one distribution center

        dist_center = ""
        for i in range(1, nodeNumber + 1, 1): 
            #nodes are stored as nodetage, attribute, set, and stores will have a corresponding distribution center tag
            disjointsets[file_data[i].split()[0]] = [file_data[i].split()[0], file_data[i].split()[1], file_data[i].split()[0], ""]
            
            if ( file_data[i].split()[0][0] == "d" ):
                dist_center = file_data[i].split()[0]
            elif ( file_data[i].split()[0][0] == "s" ): 
                # print(dist_center)
                disjointsets[file_data[i].split()[0]] = [file_data[i].split()[0], file_data[i].split()[1], file_data[i].split()[0], disjointsets[dist_center][0]]

            # we hold information on what type of node this is as well as the set this node belongs to 

        edgeLinkedList = []

        for i in range(1 + nodeNumber, 1 + nodeNumber + edgeNumber, 1): 
            # print("i: " + str(i) + "file_data: " + file_data[i])
            # second part of if statement was added after we fixed DCS linked: (reverse check edges) 
            
            # print("edge:  " + file_data[i].split()[0] + "cont: " + file_data[i].split()[1])

            if ( ( (file_data[i].split()[0][0] == "p" or file_data[i].split()[0][0] == "r" ) and file_data[i].split()[1][0] == "s" ) or ( file_data[i].split()[0][0] == "s" and (file_data[i].split()[1][0] == "p" or file_data[i].split()[1][0] == "r" ) )): 
                # print( "check1 " + file_data[i] )
                continue; 
                # this check eliminates connections from ports/rail-hubs to stores

            #distribution center check: 
            # fixed test case DCS linked
            if ( file_data[i].split()[0][0] == "d" and file_data[i].split()[1][0] == "d" ): 
                continue; 

            if ( (file_data[i].split()[0][0] == "d" and file_data[i].split()[1][0] == "s" ) ): 
                # print( "check2 " + file_data[i] )
                # store = filter(lambda store: store.distributionCenter == file_data.split()[0][0], disjointsets)
                # if ( store.__sizeof__ == 0 ): 
                #     print( "check2exec " + file_data[i])
                #     continue

                # lets try something else: 
                # print("disjointsets' dist center for store" + disjointsets[file_data[i].split()[1]][3])
                # print("distcenter " + file_data[i].split()[0])
                if (disjointsets[file_data[i].split()[1]][3] != file_data[i].split()[0]): 
                    continue

            # added after we fixed DCS linked: (reverse check edges) 
            if ( ( file_data[i].split()[0][0] == "s" and file_data[i].split()[1][0] == "d" ) ): 
                # print( "check2 " + file_data[i] )
                # store = filter(lambda store: store.distributionCenter == file_data.split()[1][0], disjointsets)
                # if ( store.__sizeof__ == 0 ): 
                #     print( "check2exec " + file_data[i])
                #     continue

                # lets try something else: 
                # print("disjointsets' dist center for store" + disjointsets[file_data[i].split()[0]][3])
                # print("distcenter " + file_data[i].split()[1])
                if (disjointsets[file_data[i].split()[0]][3] != file_data[i].split()[1]): 
                    continue

            edgeLinkedList.append([file_data[i].split()[0], file_data[i].split()[1], file_data[i].split()[2]]) 
            # in our "linkedList" storage of edges from nodes, we have info on the two edges of the nodes and the weight
        

        # print(disjointsets)
        # print(edgeLinkedList)

        # your function to compute the result should be called here

        return self.kruskal(disjointsets, edgeLinkedList)

    def kruskal(self, disjointsets, edgeLinkedList): 
        edgesAccepted = 0
        cumulativeWeight = 0
        queue = sorted(edgeLinkedList, key = lambda i : i[2]) 
        #print(queue)

        while (edgesAccepted < len(disjointsets) - 1): 
            e = queue.pop(0)
            u = e[0]
            v = e[1]

            # print("u: " + u)
            # print("v: " + v)

            #finding the set of u
            uset = disjointsets[u][2]
            while ( uset != disjointsets[uset][2] ):
                uset = disjointsets[uset][2]

            vset = disjointsets[v][2]
            while ( vset != disjointsets[vset][2] ):
                vset = disjointsets[vset][2]

            # print("uset: " + uset)
            # print("vset: " + vset)

            if (uset != vset ): 
                edgesAccepted+=1
                disjointsets[uset][2] = vset
                print("u: " + u + " v: " + v + " weight: " + e[2] )
                cumulativeWeight += int(e[2])

            # print(edgesAccepted)
            # print(len(disjointsets) - 1)    
            # print("cumWeight: " + str(cumulativeWeight) )        
        
        return cumulativeWeight



