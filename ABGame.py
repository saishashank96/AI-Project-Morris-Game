# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:40:51 2022

@author: kondu
"""


from MiniMaxOpening import CloseMill
from MiniMaxOpening import GenerateRemove
from MiniMaxOpening import CloseMill2
from MiniMaxOpening import GenerateMove
from MiniMaxOpening import staticEstimateMid
from MiniMaxOpening import GenerateMovesMidgameEndgame


class solution:
    def __init__(self):
        self.counter=0
        self.min_estimate=0
    def minmax(self,input1,depth,min1,max1):
    
    
           # estimate=staticEstimateOpen(input1)
          #  return estimate
        if depth>0:
            min_val=float('-inf')

            allpossible=GenerateMovesMidgameEndgame(input1)
                
            depth=depth-1
            for i in allpossible:
                input2=self.minmax2(i,depth,min1,max1)
                
                if min_val< staticEstimateMid(input2):
                    min_val=staticEstimateMid(input2)
                    self.min_estimate=min_val
    
                    output=i
                if max1<=min_val:
                    return output
                else:
                    min1= min_val if min_val >min1 else min1
                
            return output
        else:
            self.counter+=1
        return input1
    
    def minmax2(self,input1,depth,min1,max1):
    
    
           # estimate=staticEstimateOpen(input1)

          #  return estimate
        if depth>0:
            input1=input1.replace('W','k')
            input1=input1.replace('B','W')
            input1=input1.replace('k','B')
            allpossible2=[]
            allpossible=GenerateMovesMidgameEndgame(input1)
            for j in allpossible:
                j=j.replace('W','k')
                j=j.replace('B','W')
                j=j.replace('k','B')
                allpossible2.append(j)  
            
            
            min_val=float('inf')
            
            depth=depth-1
            for i in allpossible2:
                input2=self.minmax(i,depth,min1,max1)
                
                if min_val> staticEstimateMid(input2):
                    min_val=staticEstimateMid(input2)
                    
    
                    output=i
                if min1>=min_val:
                    return output
                else:
                    max1= min_val if min_val <max1 else max1
                    
            return output
        else:
            self.counter+=1
        return input1



import sys
def GenerateMovesOpening(input1):

    #input1="xWxxxWxxBxxxxxBxxx"
    depth=int(sys.argv[3])
    obj=solution()
    output=obj.minmax(input1,depth,float('-inf'),float('inf'))
    print('Board Position:',output) 
    print('Positions evaluated by static estimation:',obj.counter)
    print('MINIMAX estimate:',obj.min_estimate)
    with open(sys.argv[2], 'w') as f:
        f.write(output)    
if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
            input1 = f.read()
    print(input1)
    GenerateMovesOpening(str(input1))