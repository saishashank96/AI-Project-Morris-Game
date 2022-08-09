# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:01:38 2022

@author: kondu
"""

from MiniMaxOpening import staticEstimateOpen
from MiniMaxOpening import GenerateAdd        
        
class solution:
    def __init__(self):
        self.counter=0
        self.min_estimate=0
        self.counter1=0
       # self.all=[]
    def minmax(self,input1,depth):
        
        if depth>0:
            min_val=float('-inf')

                
            allpossible=GenerateAdd(input1,'B')
            
           # print(len(allpossible))  
           # print(allpossible)
            depth=depth-1
            for i in allpossible:
               # self.all.append(i)
                input2=self.minmax2(i,depth)
                static=staticEstimateOpen(input2)
                if min_val< static:
                    min_val=static
                    self.min_estimate=min_val
    
                    output=i#here
            
            return output
        elif depth==0:
            self.counter+=1
        return input1
    def minmax2(self,input1,depth):
        if depth>0:
            input1=input1.replace('W','k')
            input1=input1.replace('B','W')
            input1=input1.replace('k','B')
            allpossible2=[]
            allpossible=GenerateAdd(input1,'B')#and here
            
            for j in allpossible:
                j=j.replace('W','k')
                j=j.replace('B','W')
                j=j.replace('k','B')
                allpossible2.append(j)
            #self.all+=allpossible2
            min_val=float('inf')
           # print(allpossible2)
            depth=depth-1
            for i in allpossible2:
                #self.all.append(i)
                input2=self.minmax(i,depth)
                static=staticEstimateOpen(input2)
                if min_val> static:
                    min_val=static
    
                    output=i #here
            return output
        elif depth==0:
            self.counter+=1
        return input1

            
            
        
        
import sys
def GenerateMovesOpening(input1):
    
    depth=int(sys.argv[3])
    #input1="xxxxxxxWxxxxxxxxxx"
    input1=input1.replace('W','k')
    input1=input1.replace('B','W')
    input1=input1.replace('k','B')    
    #depth=1
    obj=solution()
    input1=obj.minmax(input1,depth)
    input1=input1.replace('W','k')
    input1=input1.replace('B','W')
    input1=input1.replace('k','B')  
    print('Board Position:',input1) 
    print('Positions evaluated by static estimation:',obj.counter)
    print('MINIMAX estimate:',obj.min_estimate)
    output=input1
    with open(sys.argv[2], 'w') as f:
        f.write(output)   
if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
            input1 = f.read()
    #print(input1)
    GenerateMovesOpening(str(input1))
    

