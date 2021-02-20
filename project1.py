"""
Project 1 ENPM661: Planning for Autonomous Robots
Author: Vivek Sood - 117504279

This python script is used to solve a n x n
sliding number puzzle.

The algorithm I have implemented uses a priority
queue that optimizes the brute force bfs approach.

For example: For testcase5 the code is 25.2 times
faster with around 15.3 times fewer iterations.

"""


# Importing all the required packages and libraries

import numpy as np
import time
import copy


class PriorityQueue:
    """
    Class created to implement priority queue

    Maintains a list of nodes with another list
    maintaining the priority of each node.

    """

    def __init__(self, node):
        """
        Initialize a PriorityQueue object corresponding to a
        test-case.

        Note the initial queue has the test-case provided
        and the priorityList is given a priority of 1(any
        value works) for the testcase provided.

        Input: node/testCase(np.array)

        Return:

        """
        self.queue = [node]
        self.priorityList = [1]

    def extentOfArrangement(self, node):
        """
        Generate a priority number for each node by the extent of
        arrangement i.e., checking how many elements are inplace
        when compared to the goal state.

        Input: self,testCase/node

        Returns: Priority of the input node

        """
        priority = 0
        for index, element in enumerate(node):
            if((index + 1) == element):
                priority += 1
        return priority

    def insert(self, node):
        """
        Insert an element in the queue and also store its
        priority generated using the extentOfArrangement.

        Input: self,testCase/node

        Returns:

        """
        priority = self.extentOfArrangement(node)
        self.queue.append(node)
        self.priorityList.append(priority)

    def extract(self):
        """
        Pop a testCase/node which has the max priority
        from the queue.

        Input:

        Returns: The node with the maximum
        priority(np.array)

        """
        index = self.priorityList.index(max(self.priorityList))
        self.priorityList.pop(index)
        return self.queue.pop(index)


class Tile:
    """
    Class that is used to do tile operation processing
    which includes generating possible moves for the
    blank tile using the current testCase/node

    """

    def __init__(self, node, visited, size):
        """
        Initialize a Tile object corresponding to a
        test-case, an empty Dictionary which would
        hold the visted nodes as the iterations
        begin, and the size of the puzzle.

        Input: node/testCase(np.array), visited(Dict),
        size(int)

        Return:

        """

        self.queue = PriorityQueue(node)
        self.visited = visited
        self.results = []

        # Generating the goal node
        self.goal = np.append(np.array([i for i in range(1, size)]), 0)

        # Calculation the size of puzzle.
        self.size = np.sqrt(size)

    def tileMover(self, node, index, indexWithOperation):
        """
        Generate the next node based on the operation and
        the node

        Input: node/testCase(np.array), index(int),
        indexWithOperation(int)

        Return: the new node(np.array)

        """
        node = copy.deepcopy(node)
        # swapping places
        node[indexWithOperation], node[index] = 0, node[indexWithOperation]
        return node

    def tileProcessor(self):
        """
        Process the tile opertion and check if the
        goal node is achived or not.

        Input: self

        Return: flag(Boolean)

        """

        queue = self.queue

        #popping an element from the queue
        node = queue.extract()
        self.results.append(node)
        size = int(self.size)
        visited = self.visited

        # finding the blank tile 
        index = np.where(node == 0)[0]

        # Location of the blank
        column, row = divmod(index, size)
        
        # Used to move the blank tile.
        indexMinusSize = index - size
        indexPlusSize = index + size
        indexMinusOne = index - 1
        indexPlusOne = index + 1

        if(column != 0):
            left = self.tileMover(node, index, indexMinusSize)
            if(np.array_equal(self.goal, left)):
                return True

            forVisited = tuple(left)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.insert(left)

        if(column != size - 1):
            right = self.tileMover(node, index, indexPlusSize)
            if(np.array_equal(self.goal, right)):
                return True

            forVisited = tuple(right)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.insert(right)

        if(row != 0):
            top = self.tileMover(node, index, indexMinusOne)
            if(np.array_equal(self.goal, top)):
                return True

            forVisited = tuple(top)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.insert(top)

        if(row != size - 1):
            down = self.tileMover(node, index, indexPlusOne)
            if(np.array_equal(self.goal, down)):
                return True

            forVisited = tuple(down)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.insert(down)

        return False


def main():
    print(r"""
    ____                  __
   / __ \__  __________  / /__
  / /_/ / / / /_  /_  / / / _ \
 / ____/ /_/ / / /_/ /_/ /  __/
/_/____\__,_/ /\\_/___/_/\___/
  / ___/____  / /   _____  _____
  \__ \/ __ \/ / | / / _ \/ ___/
 ___/ / /_/ / /| |/ /  __/ /
/____/\____/_/ |___/\___/_/
""")

    start = time.time()

    # Uncomment the testCases you need to run and comment the uncommented testcase

    # testCase1 = np.array([[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]])
    # flatenedList = testCase1.flatten()

    # testCase2 = np.array([[1, 0, 3, 4], [5, 2, 7, 8], [9, 6, 10, 11], [13, 14, 15, 12]])
    # flatenedList = testCase2.flatten()

    # testCase3 = np.array([[0, 2, 3, 4], [1, 5, 7, 8], [9, 6, 11, 12], [13, 10, 14, 15]])
    # flatenedList = testCase3.flatten()

    # testCase4 = np.array([[5, 1, 2, 3], [0, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]])
    # flatenedList = testCase4.flatten()

    testCase5 = np.array([[1, 6, 2, 3], [9, 5, 7, 4], [0, 10, 11, 8], [13, 14, 15, 12]])
    flatenedList = testCase5.flatten()

    # some additional testcases

    # testCase6 = np.array([[1, 5, 9, 13], [2, 6, 10, 14], [3, 0, 7, 11], [4, 8, 12, 15]])
    # flatenedList = testCase6.flatten()

    # test-case for a 3x3 puzzle

    # testCase7 = np.array([[8,7,6],[5,4,3],[2,1,0]])
    # flatenedList = testCase7.flatten()

    # test-case for a 5x5 puzzle

    # testCase8 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[0,22,23,21,24]])
    # flatenedList = testCase8.flatten()


    tile = Tile(flatenedList, {}, len(flatenedList))

    flag = False
    steps = 0

    while(not flag):
        steps += 1
        flag = tile.tileProcessor()

    end = time.time()

    # Writing the output to a file
    f = open("nodePath.txt", "w+")
    f.write("\nThe steps taken by the program are:\n\n")
    sizeOfProblem = int(tile.size)
    for index, ele in enumerate(tile.results):
        if(index == 0):
            f.write("Start Node\n")
        else:
            f.write("Step "+str(index)+"\n")
        f.write(str(np.reshape(ele, (sizeOfProblem, sizeOfProblem)))+"\n\n")
    f.write("Step "+str(steps)+"\n")
    f.write(str(np.reshape(tile.goal, (sizeOfProblem, sizeOfProblem)))+"     Solved!!!!!!!!!!\n")

    finalOut = f"\nPuzzle solved in {round(end - start, 4)} seconds with {steps} steps.\n"
    print(finalOut)
    f.write(finalOut)
    print("Output file Generated with the relative path './nodePath.txt'", "\n")

    f.close()


if __name__ == '__main__':
    main()
