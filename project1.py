import numpy as np
import time
import copy






class Tile:

    def __init__(self,testCase):
        
        self.queue = [testCase]
        self.visitedDict = {}
        
        
    def checkAndGenerateSignature(self,testCase):
        signature = ""
        finalOutput = "01050913020610140307111504081200"
        for tile in testCase.flatten():
            tile = str(tile)
            if (len(tile) == 1):
                signature += "0" + tile
            else:
                signature += tile
        if(signature == finalOutput):
            flag = True
        else:
            flag = False
        return signature,flag

    def mover(self,x,y,testCase,signList):
        moverTestCase = copy.deepcopy(testCase)
        moverTestCase[x + signList[0]][y + signList[1]], moverTestCase[x + signList[2]][y + signList[3]] = moverTestCase[x + signList[2]][y + signList[3]], 0
        signature,flag = self.checkAndGenerateSignature(testCaseMoveTop)
        if(flag):
            return False
        elif(signature not in self.visitedDict):
            self.visitedDict[signature] = 0
            self.queue.append(testCaseMoveTop)
        return True
    

    def moveTile(self):
        testCase = self.queue.pop(0)
        x1, y1 = np.where(testCase == 0)
        
        x = x1[0]
        y = y1[0]
        matrixSize = len(testCase)
        if(y != 0):
            flag = self.mover(x,y,testCase,[0,0,0,-1])
            
        
        if(y != matrixSize-1):
            testCaseMoveDown = copy.deepcopy(testCase)
            testCaseMoveDown[x][y] = testCaseMoveDown[x][y+1]
            testCaseMoveDown[x][y+1] = 0
            signature,flag = self.checkAndGenerateSignature(testCaseMoveDown)
            if(flag):
                return False
            elif(signature not in self.visitedDict):
                self.visitedDict[signature] = 0
                self.queue.append(testCaseMoveDown)
        if(x != 0):
            testCaseMoveLeft = copy.deepcopy(testCase)
            testCaseMoveLeft[x][y] = testCaseMoveLeft[x-1][y]
            testCaseMoveLeft[x-1][y] = 0
            signature,flag = self.checkAndGenerateSignature(testCaseMoveLeft)
            if(flag):
                return False
            elif(signature not in self.visitedDict):
                self.visitedDict[signature] = 0
                self.queue.append(testCaseMoveLeft)
        if(x != matrixSize-1):
            testCaseMoveRight = copy.deepcopy(testCase)
            testCaseMoveRight[x][y] = testCaseMoveRight[x+1][y]
            testCaseMoveRight[x+1][y] = 0
            signature,flag = self.checkAndGenerateSignature(testCaseMoveRight)
            if(flag):
                return False
            elif(signature not in self.visitedDict):
                self.visitedDict[signature] = 0
                self.queue.append(testCaseMoveRight)
        
        return True

def main():
    #testCase1 = np.array([[1, 2, 3, 4],[ 5, 6, 0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]])
    testCase1 = np.array([[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,0,12]])
    tile = Tile(testCase1)
    #print(Tile.findBlankTile())
    #tile.checkAndGenerateSignature()
    flag = True
    while(flag):
        flag = tile.moveTile()
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end- start)





