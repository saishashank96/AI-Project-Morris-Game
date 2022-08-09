# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 08:56:54 2022

@author: kondu
"""
import sys

def GenerateAddHelp(input1):
    print((input1[11]))
    for i in [11,14,17,6,5,10,9,13,12,7,3,8,1,16,15,4,2,0]:
        if input1[i]=="x":
            input1=input1[:i]+'W'+input1[i+1:]
            return input1
# close mill as suggested in handout
def CloseMill(a):
    for p,q,r in [(0,2,4),(5,3,1),(6,7,8),(11,14,17),(10,13,16),(9,12,15),(15,16,17),(12,13,14),(9,10,11),(5,6,11),(3,7,14),(1,8,17)]:        
        #print(a)
       # print(p,q,r)
        if a[p]==a[q]==a[r]=='W':
           # print(p,q,r)
            return 1
    return 0



def CloseMill2(a,b):
    for p,q,r in [(0,2,4),(5,3,1),(6,7,8),(11,14,17),(10,13,16),(9,12,15),(15,16,17),(12,13,14),(9,10,11),(5,6,11),(3,7,14),(1,8,17)]:        
        if p==b or q==b or r==b:
            if a[p]==a[q]==a[r]=='B':
                #print(p,q,r)
                return 1
    return 0
def CloseMill3(a,b):
    for p,q,r in [(0,2,4),(5,3,1),(6,7,8),(11,14,17),(10,13,16),(9,12,15),(15,16,17),(12,13,14),(9,10,11),(5,6,11),(3,7,14),(1,8,17)]:        
        if p==b or q==b or r==b:
            if a[p]==a[q]==a[r]=='W':
                #print(p,q,r)
                return 1
    return 0

# return neighbours of a given point
def Neighbour(a):
    neigh={}
    neigh[0]=[1,2,15]
    neigh[1]=[0,3,8]
    neigh[2]=[0,3,4,12]
    neigh[3]=[2,1,5,7]
    neigh[4]=[2,5,9]
    neigh[5]=[4,3,6]
    neigh[6]=[11,5,7]
    neigh[7]=[6,8,3,14]
    neigh[8]=[7,1,17]
    neigh[9]=[4,10,12]
    neigh[10]=[9,11,13]
    neigh[11]=[10,6,14]
    neigh[12]=[2,9,13,15]
    neigh[13]=[12,14,10,16]
    neigh[14]=[7,11,13,17]
    neigh[15]=[0,12,16]
    neigh[16]=[15,13,17]
    neigh[17]=[14,8,16]
    
    return neigh[a]



def countit(input1,c):
    count=0
    for i in input1:
        if i == c:
            count+=1
    return count


def staticEstimateOpen(input1):
    return (countit(input1,'W')-countit(input1,'B'))



# Remove function as suggested in the handout
def GenerateRemove(input2,list1,c):
    list2=list1
    for i in range(18):
        input3=input2
        if input3[i]==c:
            if CloseMill2(input3,i):
                list2.append(input3)
            else:
                input3=input3[:i]+'x'+input3[i+1:]
                list2.append(input3)
            
    return list2  
         
            
#Add as suggested in the handout 
def GenerateAdd(input1,c):
    list1=[]
    for i in range(18):
        input2=input1
        
        if input2[i]=="x":
            input2=input2[:i]+'W'+input2[i+1:]
            if CloseMill(input2):
                #remove
                #print("hi")
                list1=GenerateRemove(input2,list1,c)
            else:
                list1.append(input2)
    return list1
                
def GenerateMove(input1):
    list1=[]
    for i in range(len(input1)):
        if input1[i]=='W':
            for j in Neighbour(i):
                if input1[j]=='x':
                    input2=input1
                    input2=input2[:i]+'x'+input2[i+1:]
                    input2=input2[:j]+'W'+input2[j+1:]
                    if CloseMill3(input2,j):
                        GenerateRemove(input2, list1, 'B')
                    else:
                        list1.append(input2)

                        
                    
    return list1

def GenerateHopping(input1):
    list1=[]
    for i in range(len(input1)):
        if input1[i]=='W':
            for j in range(len(input1)):
                if input1[j]=='x':
                    input2=input1
                    input2=input2[:i]+'x'+input2[i+1:]
                    input2=input2[:j]+'W'+input2[j+1:]
                    if CloseMill3(input2,j):
                        GenerateRemove(input2, list1, 'B')
                    else:
                        list1.append(input2)
                
        
    return list1   


             
def GenerateMovesMidgameEndgame(input1):
    if input1.count('W') >3:
        allpossible=GenerateMove(input1)
    else:
        allpossible=GenerateHopping(input1)
    return allpossible

           
def staticEstimateMid(input1):
    a=countit(input1,'W')    
    b=countit(input1,'B')
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
    if b<3:
        return 10000
    elif a<3:
        return -10000
    elif len(allpossible2)==0:
        return 10000
    else:
       # print(1000*(a-b)-len(allpossible))
        return (1000*(a-b)-len(allpossible))
        
                
            
# class solution which calculate the max and min function named as minmax and minmax2 respectively        
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

            
            
        
        
#function which calls the subprogram
def GenerateMovesOpening(input1):

    #input1="xWxxxWxxBxxxxxBxxx"
    depth=int(sys.argv[3])
    obj=solution()
    #print(input1)
    output=obj.minmax(input1,depth)
    print('Board Position:',output) 
    print('Positions evaluated by static estimation:',obj.counter)
    print('MINIMAX estimate:',obj.min_estimate)
    with open(sys.argv[2], 'w') as f:
        f.write(output)

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
            input1 = f.read()
    GenerateMovesOpening(str(input1))
    

