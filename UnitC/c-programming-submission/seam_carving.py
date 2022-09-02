# CS4102 Spring 2022 -- Unit C Programming
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

class SeamCarving:
    energyMatrix = []
    seamMatrix = []
    selectionMatrix = []


    def __init__(self):
        return

    def getEnergy(self, image, row, column): 
        # getting the energy of an interior pixel: 
        energy = 0
        pixelRed = image[row][column][0]
        pixelGreen = image[row][column][1]
        pixelBlue = image[row][column][2]

        for i in range(row - 1, row + 2): 
            for j in range( column - 1, column + 2 ): 
                if ( i == row and j == column ): 
                    continue
                energy += ( (image[i][j][0] - pixelRed)**2 + (image[i][j][1] - pixelGreen)**2 + (image[i][j][2] - pixelBlue)**2 )**(1/2) 

        energy /= 8

        return energy

    def getEnergyTopRow(self, image, column): 
        pixelRed = image[0][column][0]
        pixelGreen =  image[0][column][1]
        pixelBlue =  image[0][column][2]

        energy = 0

        for i in range (0, 2): 
            for j in range( column - 1, column + 2): 
                if ( i == 0 and j == column ): 
                    continue
                energy += ( (image[i][j][0] - pixelRed)**2 + (image[i][j][1] - pixelGreen)**2 + (image[i][j][2] - pixelBlue)**2 )**(1/2)
            
        energy /= 5

        return energy

    def getEnergyBottomRow(self, image, column): 
        pixelRed = image[len(image) - 1][column][0]
        pixelGreen =  image[len(image) - 1][column][1]
        pixelBlue =  image[len(image) - 1][column][2]

        energy = 0

        for i in range (len(image) - 2, len(image)): 
            for j in range( column - 1, column + 2): 
                if ( i == (len(image) - 1) and j == column ): 
                    continue
                energy += ( (image[i][j][0] - pixelRed)**2 + (image[i][j][1] - pixelGreen)**2 + (image[i][j][2] - pixelBlue)**2 )**(1/2)
            
        energy /= 5

        return energy

    def getEnergyLeftColumn(self, image, row): 
        pixelRed = image[row][0][0]
        pixelGreen =  image[row][0][1]
        pixelBlue =  image[row][0][2]

        energy = 0

        for i in range (row - 1, row + 2): 
            for j in range( 0, 2): 
                if ( i == row and j == 0 ): 
                    continue
                energy += ( (image[i][j][0] - pixelRed)**2 + (image[i][j][1] - pixelGreen)**2 + (image[i][j][2] - pixelBlue)**2 )**(1/2)
            
        energy /= 5

        return energy

    def getEnergyRightColumn(self, image, row): 
        pixelRed = image[row][len(image[0]) - 1][0]
        pixelGreen =  image[row][len(image[0]) - 1][1]
        pixelBlue =  image[row][len(image[0]) - 1][2]

        energy = 0

        for i in range (row - 1, row + 2): 
            for j in range( len(image[0]) - 2, len(image[0])): 
                if ( i == row and j == (len(image[0]) - 1) ): 
                    continue
                energy += ( (image[i][j][0] - pixelRed)**2 + (image[i][j][1] - pixelGreen)**2 + (image[i][j][2] - pixelBlue)**2 )**(1/2)
            
        energy /= 5

        return energy

    def getEnergyMatrix(self, image): 
        # first lets get the energy for the inner part of the image

        for i in range(1, len(image) - 1):
            for j in range(1, len(image[0]) - 1):
                self.energyMatrix[i][j] = self.getEnergy(image, i, j)

        # now the corners: 

        self.energyMatrix[0][0] = 0
        pixelRed = image[0][0][0]
        pixelGreen = image[0][0][1]
        pixelBlue = image[0][0][2]

        self.energyMatrix[0][0] += ( (image[0][1][0] - pixelRed)**2 + (image[0][1][1] - pixelGreen)**2 + (image[0][1][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[0][0] += ( (image[1][0][0] - pixelRed)**2 + (image[1][0][1] - pixelGreen)**2 + (image[1][0][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[0][0] += ( (image[1][1][0] - pixelRed)**2 + (image[1][1][1] - pixelGreen)**2 + (image[1][1][2] - pixelBlue)**2 )**(1/2) 

        self.energyMatrix[0][0] /= 3


        self.energyMatrix[0][len(image[0]) - 1] = 0
        
        pixelRed = image[0][len(image[0]) - 1][0]
        pixelGreen = image[0][len(image[0]) - 1][1]
        pixelBlue = image[0][len(image[0]) - 1][2]

        self.energyMatrix[0][len(image[0]) - 1] += ( (image[0][len(image[0]) - 2][0] - pixelRed)**2 + (image[0][len(image[0]) - 2][1] - pixelGreen)**2 + (image[0][len(image[0]) - 2][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[0][len(image[0]) - 1] += ( (image[1][len(image[0]) - 2][0] - pixelRed)**2 + (image[1][len(image[0]) - 2][1] - pixelGreen)**2 + (image[1][len(image[0]) - 2][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[0][len(image[0]) - 1] += ( (image[1][len(image[0]) - 1][0] - pixelRed)**2 + (image[1][len(image[0]) - 1][1] - pixelGreen)**2 + (image[1][len(image[0]) - 1][2] - pixelBlue)**2 )**(1/2) 

        self.energyMatrix[0][len(image[0]) - 1] /= 3


        self.energyMatrix[len(image) - 1][len(image[0]) - 1] = 0
        pixelRed = image[len(image) - 1][len(image[0]) - 1][0]
        pixelGreen = image[len(image) - 1][len(image[0]) - 1][1]
        pixelBlue = image[len(image) - 1][len(image[0]) - 1][2]

        self.energyMatrix[len(image) - 1][len(image[0]) - 1] += ( (image[len(image) - 2][len(image[0]) - 2][0] - pixelRed)**2 + (image[len(image) - 2][len(image[0]) - 2][1] - pixelGreen)**2 + (image[len(image) - 2][len(image[0]) - 2][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[len(image) - 1][len(image[0]) - 1] += ( (image[len(image) - 2][len(image[0]) - 1][0] - pixelRed)**2 + (image[len(image) - 2][len(image[0]) - 1][1] - pixelGreen)**2 + (image[len(image) - 2][len(image[0]) - 1][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[len(image) - 1][len(image[0]) - 1] += ( (image[len(image) - 1][len(image[0]) - 2][0] - pixelRed)**2 + (image[len(image) - 1][len(image[0]) - 2][1] - pixelGreen)**2 + (image[len(image) - 1][len(image[0]) - 2][2] - pixelBlue)**2 )**(1/2) 

        self.energyMatrix[len(image) - 1][len(image[0]) - 1] /= 3



        self.energyMatrix[len(image) - 1][0] = 0
        pixelRed = image[len(image) - 1][0][0]
        pixelGreen = image[len(image) - 1][0][1]
        pixelBlue = image[len(image) - 1][0][2]

        self.energyMatrix[len(image) - 1][0] += ( (image[len(image) - 2][0][0] - pixelRed)**2 + (image[len(image) - 2][0][1] - pixelGreen)**2 + (image[len(image) - 2][0][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[len(image) - 1][0] += ( (image[len(image) - 2][1][0] - pixelRed)**2 + (image[len(image) - 2][1][1] - pixelGreen)**2 + (image[len(image) - 2][1][2] - pixelBlue)**2 )**(1/2) 
        self.energyMatrix[len(image) - 1][0] += ( (image[len(image) - 1][1][0] - pixelRed)**2 + (image[len(image) - 1][1][1] - pixelGreen)**2 + (image[len(image) - 1][1][2] - pixelBlue)**2 )**(1/2) 

        self.energyMatrix[len(image) - 1][0] /= 3


        # now for the top row
        
        for j in range (1, len(image[0]) - 1): 
            self.energyMatrix[0][j] = self.getEnergyTopRow(image, j)

        # for the bottom row

        for j in range (1, len(image[0]) - 1): 
            self.energyMatrix[len(image) - 1][j] = self.getEnergyBottomRow(image, j)

        # leftmost column

        for i in range (1, len(image) - 1):
            self.energyMatrix[i][0] = self.getEnergyLeftColumn(image, i)

        # rightmost column

        for i in range (1, len(image) - 1):
            self.energyMatrix[i][len(image[0]) - 1] = self.getEnergyRightColumn(image, i)
    
    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        for i in image: 
            self.energyMatrix.append([0] * len(image[0]))
            self.seamMatrix.append([0] * len(image[0]))
            self.selectionMatrix.append([0] * len(image[0]))
        
        self.getEnergyMatrix(image)
        
        print("len(image) = ", len(image))
        print("len(image[0] = ", len(image[0]) )


        # for i in range(0, len(image)): 
        #     for j in range(0, len(image[0])): 
        #         print(image[i][j][0], image[i][j][1], image[i][j][2], end = '|')
        #     print("\n")


        # for i in range(0, len(image)): 
        #     for j in range(0, len(image[0])): 
        #         print(self.energyMatrix[i][j], end = '|')
        #     print("")

        # initialize the seams at the bottom row (len(image) - 1)
        for i in range(0, len(image[0])): 
            self.seamMatrix[len(image) - 1][i] = self.energyMatrix[len(image) - 1][i]

        # loop to compute seam weight
        for i in reversed(range(0, len(image) - 1)): # have to do this in reverse
            for j in range(0, len(image[0])): 

                # print ("i: ", i , " j: ", j, end = "|")
                
                best = 10000000000000

                if (j == 0): 
                    for k in range(0, 2): 
                        if ( self.seamMatrix[i + 1][k] + self.energyMatrix[i][j] < best ): 
                            best = self.seamMatrix[i + 1][k] + self.energyMatrix[i][j]
                            self.seamMatrix[i][j] = best
                            self.selectionMatrix[i][j] = k
                    continue

                if (j == len(image[0]) - 1): 
                    for k in range(j - 1, j + 1): 
                        if ( self.seamMatrix[i + 1][k] + self.energyMatrix[i][j] < best ): 
                            best = self.seamMatrix[i + 1][k] + self.energyMatrix[i][j]
                            self.seamMatrix[i][j] = best
                            self.selectionMatrix[i][j] = k
                    continue

                for k in range(j - 1, j + 2): 
                    # print("i: ", i, " j: ", j)
                    if ( self.seamMatrix[i + 1][k] + self.energyMatrix[i][j] < best ): 
                        best = self.seamMatrix[i + 1][k] + self.energyMatrix[i][j]
                        self.seamMatrix[i][j] = best
                        self.selectionMatrix[i][j] = k
            print("/n")

        for i in range(0, len(image)): 
            for j in range(0, len(image[0])): 
                print(self.seamMatrix[i][j], end = '|')
            print("\n")

        for i in range(0, len(image)): 
            for j in range(0, len(image[0])): 
                print(self.selectionMatrix[i][j], end = '|')
            print("\n")

        # now to find the minimum weight seam
        best = 100000000
        for i in range(len(image[0])): 
            
            print (self.seamMatrix[len(image) - 1][i], end = "|")
            if ( self.seamMatrix[0][i] < best ): 
                best = self.seamMatrix[0][i]

        return best

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        result = []

        # first we have to find the column where the smallest seam ends
        best = 100000000
        index = 0
        for i in range(len(self.energyMatrix[0])): 
            if ( self.seamMatrix[0][i] < best ): 
                index = i
                best = self.seamMatrix[0][i]

        result.append(index)

        for i in range(0, len(self.energyMatrix) - 1): # switched from - 2 to - 1
            result.append(self.selectionMatrix[i][index])
            index = self.selectionMatrix[i][index]

        # best = 100000000
        # for i in range(result[len(result) - 1] - 1, result[len(result) - 1] + 2): 
        #     if ( self.energyMatrix[len(self.energyMatrix) - 1][i] < best ): 
        #         index = i
        #         best = self.seamMatrix[len(self.energyMatrix) - 1][i]

        # result.append(index)

        return result

