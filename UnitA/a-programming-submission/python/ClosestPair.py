from cProfile import run
from lib2to3.pgen2.token import NOTEQUAL
import math
from statistics import median
import statistics
# CS4102 Spring 2022 - Unit A Programming 
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

import numpy as np

class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1 
    def compute(self, file_data):
        pointArray = []
        for i in file_data:
            pointArray.append( [ float(i.split()[0]), float(i.split()[1]) ] )

        npPointArray = np.array(pointArray)

        npPointArray = npPointArray[ np.argsort( npPointArray[:, 0] ) ]
        npPointArray2 = npPointArray

        #print("npPointArray: ", npPointArray)
        #[closest, secondClosest] = ClosestPair.bruteForce(pointArray)

        closest = ClosestPair.recursiveCompute(npPointArray)
        closest2 = ClosestPair.recursiveCompute2(npPointArray2, closest)

        return [closest, closest2]

    def recursiveCompute2(arrayOfArrayOfPoints, closest): 
        if ( len(arrayOfArrayOfPoints) <= 2 ): 
            return ClosestPair.distanceBetween2(arrayOfArrayOfPoints[0], arrayOfArrayOfPoints[1], closest) # here we just return an arbitrarily large number as the second minimum distance.
        if ( len(arrayOfArrayOfPoints) == 3 ): 
            return ClosestPair.bruteForceSingle2(arrayOfArrayOfPoints, closest)
  
        # now we're going to assume the non-base case here: 

        x_medianValue = np.median(arrayOfArrayOfPoints, axis = 0)[0] 

        #print("arrayOfArrayOfpoints: ", arrayOfArrayOfPoints)
        leftPointArray = arrayOfArrayOfPoints[0:len(arrayOfArrayOfPoints)//2]
        rightPointArray = arrayOfArrayOfPoints[len(arrayOfArrayOfPoints)//2:]

        #print("leftPointArray: ", leftPointArray)
        #print("rightPointArray: ", rightPointArray)

        min1 = 1000

        recurseComputeLeft = ClosestPair.recursiveCompute2(leftPointArray, closest)
        recurseComputeRight = ClosestPair.recursiveCompute2(rightPointArray, closest)

        if ( recurseComputeLeft < recurseComputeRight ): 
            #if ( ClosestPair.recursiveCompute(leftPointArray) == 0 ): 
                #print("0 here: top", leftPointArray)
            min1 = recurseComputeLeft
        else: 
            #if ( ClosestPair.recursiveCompute(rightPointArray) == 0 ): 
                #print("0 here: bot", rightPointArray)
            min1 = recurseComputeRight

        checker = False
        runway = []

        for i in arrayOfArrayOfPoints: 
            if(not checker): 
                if i[0] < x_medianValue - min1: 
                    continue
                else: 
                    checker = True
                    runway.append(i)
            elif ( checker ): 
                if i[0] > x_medianValue + min1: 
                    break
                else: 
                    runway.append(i)

        runway = np.array(runway)
        runwaySorted = runway[ np.argsort( runway[:, 1] ) ]

        runwayMin1 = min1

        for j in range(0, len(runwaySorted)-1): 
            for i in range(j + 1, min( len(runwaySorted-1), j + 15 ) ): 
                distBetween = ClosestPair.distanceBetween2(runwaySorted[j], runwaySorted[i], closest)
                if ( runwayMin1 > distBetween ): 
                    #if (ClosestPair.distanceBetween(runwaySorted[j], runwaySorted[i]) == 0): 
                        #print("j, i: ", runwaySorted[j], runwaySorted[i])
                    runwayMin1 = distBetween

        return runwayMin1

    def distanceBetween2(point1, point2, closest): 
        if ( closest == math.sqrt( ((point1[0] - point2[0] )**2) + ((point1[1] - point2[1] )**2) ) ): 
            return 1000000
        return math.sqrt( ((point1[0] - point2[0] )**2) + ((point1[1] - point2[1] )**2) )

    def bruteForceSingle2(pointArray, closest):
        min_dist = 1000000000
        for i in range(0, len(pointArray) - 1): 
            for j in range(i + 1, len(pointArray) ): 
                temp = ClosestPair.distanceBetween(pointArray[i], pointArray[j])
                if (min_dist > temp): 
                    min_dist = temp

        #print("pointarray, mindist: " , pointArray, min_dist)

        if ( closest == min_dist ): 
            return 100000000000

        return min_dist


    def recursiveCompute(arrayOfArrayOfPoints): 
        if ( len(arrayOfArrayOfPoints) <= 2 ): 
            #if (ClosestPair.distanceBetween(arrayOfArrayOfPoints[0], arrayOfArrayOfPoints[1]) == 0): 
                #print("0 in recursive comptue top: ", arrayOfArrayOfPoints)
            return ClosestPair.distanceBetween(arrayOfArrayOfPoints[0], arrayOfArrayOfPoints[1]) # here we just return an arbitrarily large number as the second minimum distance.
        if ( len(arrayOfArrayOfPoints) == 3 ): 
            #if (ClosestPair.bruteForceSingle(arrayOfArrayOfPoints) == 0):
                #print("0 in recursive compute top2: ", arrayOfArrayOfPoints)
            return ClosestPair.bruteForceSingle(arrayOfArrayOfPoints)
  
        # now we're going to assume the non-base case here: 

        x_medianValue = np.median(arrayOfArrayOfPoints, axis = 0)[0] 

        #print("arrayOfArrayOfpoints: ", arrayOfArrayOfPoints)
        leftPointArray = arrayOfArrayOfPoints[0:len(arrayOfArrayOfPoints)//2]
        rightPointArray = arrayOfArrayOfPoints[len(arrayOfArrayOfPoints)//2:]

        #print("leftPointArray: ", leftPointArray)
        #print("rightPointArray: ", rightPointArray)

        min1 = 1000

        recurseComputeLeft = ClosestPair.recursiveCompute(leftPointArray)
        recurseComputeRight = ClosestPair.recursiveCompute(rightPointArray)

        if ( recurseComputeLeft < recurseComputeRight ): 
            #if ( ClosestPair.recursiveCompute(leftPointArray) == 0 ): 
                #print("0 here: top", leftPointArray)
            min1 = recurseComputeLeft
        else: 
            #if ( ClosestPair.recursiveCompute(rightPointArray) == 0 ): 
                #print("0 here: bot", rightPointArray)
            min1 = recurseComputeRight

        checker = False
        runway = []

        for i in arrayOfArrayOfPoints: 
            if(not checker): 
                if i[0] < x_medianValue - min1: 
                    continue
                else: 
                    checker = True
                    runway.append(i)
            elif ( checker ): 
                if i[0] > x_medianValue + min1: 
                    break
                else: 
                    runway.append(i)

        runway = np.array(runway)
        runwaySorted = runway[ np.argsort( runway[:, 1] ) ]

        runwayMin1 = min1

        for j in range(0, len(runwaySorted)-1): 
            for i in range(j + 1, min( len(runwaySorted-1), j + 15 ) ): 
                distBetween = ClosestPair.distanceBetween(runwaySorted[j], runwaySorted[i])
                if ( runwayMin1 > distBetween ): 
                    #if (ClosestPair.distanceBetween(runwaySorted[j], runwaySorted[i]) == 0): 
                        #print("j, i: ", runwaySorted[j], runwaySorted[i])
                    runwayMin1 = distBetween

        return runwayMin1

    def distanceBetween3Points(arrayOfArrayOfPoints): 
        min1 = 1000000
        
        for j in range(len(arrayOfArrayOfPoints)): 
            for i in arrayOfArrayOfPoints[j:]: 
                if ( min1 > ClosestPair.distanceBetween(i, arrayOfArrayOfPoints[j])): 
                    min1 = ClosestPair.distanceBetween(i, arrayOfArrayOfPoints[j])

        return min1

    # helper method to find the distance between a pair of points (assumed points are passed in as a 2 dimensional array)
    def distanceBetween(point1, point2 ): 
        return math.sqrt( ((point1[0] - point2[0] )**2) + ((point1[1] - point2[1] )**2) )

    def bruteForceSingle(pointArray):
        min_dist = 1000000000
        for i in range(0, len(pointArray) - 1): 
            for j in range(i + 1, len(pointArray) ): 
                temp = ClosestPair.distanceBetween(pointArray[i], pointArray[j])
                if (min_dist > temp): 
                    min_dist = temp

        #print("pointarray, mindist: " , pointArray, min_dist)
        return min_dist




    def bruteForce(self, pointArray): 
        cp = ClosestPair()
        closest = ClosestPair.distanceBetween( pointArray[0], pointArray[1] ); 
        secondClosest = ClosestPair.distanceBetween( pointArray[0], pointArray[2] )

        for i in pointArray: 
            for j in pointArray: 
                if (j[0] == i[0]) & (j[1] == i[1]):
                    continue

                dist = ClosestPair.distanceBetween( i, j )
                
                if (dist < closest): 
                    secondClosest = closest
                    closest = dist
                elif (dist < secondClosest):
                    secondClosest = dist

        return closest, secondClosest
