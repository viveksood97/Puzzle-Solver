import numpy as np
import time
import copy


    
class Tile:

    def __init__(self,queue,visited,size):
        self.queue = queue
        self.visited = visited
        self.result = np.append(np.array([i for i in range(1,16)]),0)
        self.size = np.sqrt(size)
        
    

    def tileMover(self):
        queue = self.queue
        testCase = queue.pop(0)
        
        
        visited = self.visited

        index = np.where(testCase == 0)[0]
        column,row = divmod(index,4)

        indexMinusFour = index - 4
        indexPlusFour  = index + 4
        indexMinusOne  = index - 1
        indexPlusOne   = index + 1

        if(column != 0):
            left = copy.deepcopy(testCase)
            left[indexMinusFour], left[index] = 0, left[indexMinusFour]

            if(np.array_equal(self.result,left)):
                return True

            forVisited = tuple(left)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.append(left)

        if(column != self.size - 1):
            right = copy.deepcopy(testCase)
            right[indexPlusFour], right[index] = 0, right[indexPlusFour]

            if(np.array_equal(self.result,right)):
                return True

            forVisited = tuple(right)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.append(right)
                
        if(row != 0):
            top = copy.deepcopy(testCase)
            top[indexMinusOne], top[index] = 0, top[indexMinusOne]

            if(np.array_equal(self.result,top)):
                return True
            
            forVisited = tuple(top)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.append(top)

        if(row != self.size - 1):
            down = copy.deepcopy(testCase)
            down[indexPlusOne], down[index] = 0, down[indexPlusOne]

            if(np.array_equal(self.result,down)):
                return True
        
            forVisited = tuple(down)
            if(forVisited not in visited):
                visited[forVisited] = 0
                queue.append(down)
        
        return False
        #print(left,right,top,down)
        

        











def main():
    testCase1 = np.array([[1, 2, 3, 4],[5, 6, 0, 8],[9, 10, 7, 12],[13, 14, 11, 15]])
    testCase2 = np.array([[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]])
    testCase3 = np.array([[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]])
    testCase4 = np.array([[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]])
    testCase5 = np.array([[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]])
    
    tile = Tile([testCase5.flatten()],{},16)
    flag = False
    steps = 0
    while(not flag):
        steps += 1
        flag = tile.tileMover()
    print(steps)  

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end- start)