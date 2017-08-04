import sys
class Node: 
  ''' Nodes representing Sudoku Grid '''
  def __init__(self,down=None,right=None,N=None,S=None,W=None,E=None,NE=None,NW=None,SE=None,SW=None,maxdepth=None,size=None,val=None):
    self.down=down  #Use to traverse in veritcal direction
    self.right=right    #Use to traverse in horizontal direction
    #Neighbours in Cardinal Directions
    self.N=N    
    self.S=S    
    self.W=W    
    self.E=E    
    self.NE=NE  
    self.NW=NW  
    self.SE=SE
    self.SW=SW
    #Longest Path
    self.maxdepth=maxdepth
    #Value of Sudoku Grid
    self.val=val
    self.size=size
    
class Sudoku:
  ''' Converts a Sudoku Grid into a Graph'''
  def __init__(self):
    self.head=None
    
  def initialize(self,Arr):
    ''' Creates a graph of the size of the given sudoku grid '''
    #gets the column/row size of grid
    col= len(Arr[0])
    row= len(Arr)
    self.head=Node()
    currRow=self.head
    currCol=currRow
    #creates first row
    for i in range(1,col):
      currCol.right=Node()
      currCol=currCol.right
    
    for j in range(1,row):
      
      currRow.down=Node()  
      currRow=currRow.down      
      currCol=currRow
      
      
      #creates nodes for jth row      
      for i in range(1,col):
        currCol.right=Node()
        currCol=currCol.right
  
  def BrainSurgery(self):
    ''' Creates links with neighbors in cardinal directions'''
    #Current Row
    rowCurr=self.head   
    #Current Column
    colCurr=self.head
    #For first row
    while colCurr.right != None:
      #Previous Column
      colPrev=colCurr
      colCurr=colCurr.right
      #Creates links between left neigbor
      colPrev.W=colCurr
      colCurr.E=colPrev
      #Creates links between NE neigbor
      if colCurr.E.N!=None:
        colCurr.E.N.SW=cc
        colCurr.NE=colCurr.E.N
        #Creates links between neigbor above
        if colCurr.E.N.W!=None:
          colCurr.E.N.W.S = cc
          colCurr.N=colCurr.E.N.W
          #Creates links between NW neigbor  
          if colCurr.E.N.W.W !=None:
            colCurr.E.N.W.W.SE=cc
            colCurr.NW=colCurr.E.N.W.W
    #for the rest of the rows        
    colCurr=rowCurr    
    i=0
    while rowCurr.down != None or colCurr.right != None:
      i=i+1
     
      if rowCurr.down != None:
        #Previous Row
        rowPrev=rowCurr
        rowCurr=rowCurr.down
        rowCurr.N=rowPrev
        rowPrev.S=rowCurr
        colCurr=rowCurr
      
      while colCurr.right != None:
        colPrev=colCurr
        colCurr=colCurr.right
        #Creates links between left neighbor
        colPrev.W=colCurr
        colCurr.E=colPrev
        #Creates links between NE neighbor
        if colCurr.E.N!=None:
          colCurr.E.N.SW=colCurr
          colCurr.NE=colCurr.E.N
          #Creates links between neighbor above
          if colCurr.E.N.W!=None:
            colCurr.E.N.W.S = colCurr
            colCurr.N=colCurr.E.N.W
          #Creates links between left neigbor
            if colCurr.E.N.W.W !=None:
              colCurr.E.N.W.W.SE=colCurr
              colCurr.NW=colCurr.E.N.W.W
    
  def insert(self,Arr):
    ''' fills graph with sudoku grid values '''
    currCol=self.head
    currRow=currCol
    j=0
    for j in range(0,len(Arr)):
      for i in range(0,len(Arr[0])):
        currCol.val=Arr[j][i]
        
        
        currCol=currCol.right
      currRow=currRow.down  
      currCol=currRow
      
  def linkcut(self,Arr):
   ''' cuts links where edge between nodes do not exist
        An edge exists between two nodes if the neighbor
        of a node is 1 higher. e.g. 6->7 form an edge, 
        7-5 do not. Neighbors being considered are all 8 
        grids that surround the "current" grid
   '''
    currCol=self.head
    currRow=currCol
    j=0
    for j in range(0,len(Arr)):
      for i in range(0,len(Arr[0])):
        if currCol=N != None:
          if currCol=val - currCol=N.val != -1:
            currCol=N=None
        if currCol=E != None:
          if currCol=val - currCol=E.val != -1:
            currCol=E=None
        if currCol=W != None:    
          if currCol=val - currCol=W.val != -1:
            currCol=W=None
        if currCol=S != None:    
          if currCol=val - currCol=S.val != -1:
            currCol=S=None
        if currCol=NE != None:    
          if currCol=val - currCol=NE.val != -1:
            currCol=NE=None
        if currCol=NW != None:    
          if currCol=val - currCol=NW.val != -1:
            currCol=NW=None
        if currCol=SE != None:    
          if currCol=val - currCol=SE.val != -1:
            currCol=SE=None
        if currCol=SW != None:    
          if currCol=val - currCol=SW.val != -1:
            currCol=SW=None
        
        currCol=currCol.right
      currRow=currRow.down  
      currCol=currRow
      
  def depth(self,root):
    ''' Find the longest monotonically increasing path for any given node'''
    if root == None:
        return 0
    
    depthN=depth(root.N)
    depthE=depth(root.E)
    depthW=depth(root.W)
    depthS=depth(root.S)
    depthNE=depth(root.NE)
    depthNW=depth(root.NW)
    depthSE=depth(root.SE)
    depthSW=depth(root.SW)
    return 1+max(depthN,depthE,depthW,depthS,depthNE,depthNW,depthSE,depthSW)
    
  def maxlink(self,graph,Arr):
    '''Runs depth() for all the grids on the sudoku'''
    root= graph.head
    currCol=root
    currRow=currCol
    j=0
    A=[]
    for j in range(0,len(Arr)):
        B=[]
        for i in range(0,len(Arr[0])):
            currCol=maxdepth=depth(ccol)
            B.append(currCol=maxdepth)
            sys.stdout.write(str(currCol=maxdepth))
            sys.stdout.write(" ")  
            currCol=currCol.right
            currRow=crow.down  
            currCol=crow
            A.append(B)
            print(" ")
    return A  

if __name__ == '__main__':
    '''Test Case
    uses the Soduku Puzzle T as input and finds longest path. 
    Then uses the longest paths for each grid as an input to a new puzzle and finds the longest path for that.
    Repeat until it gets boring.
    <Will do a Mathematical Analysis of the number of iterations needed to attain steady state later.>
    '''
    T=[[8,7,5,3,9,6,1,4,2],[4,6,1,7,8,2,9,3,5],[2,3,9,4,5,1,6,8,7],[3,2,6,8,4,5,7,9,1],[9,1,8,6,3,7,2,5,4],[7,5,4,2,1,9,3,6,8],[1,9,3,5,2,4,8,7,6],[5,8,7,1,6,3,4,2,9],[6,4,2,9,7,8,5,1,3]]


    for i in range(0,4):
        print ""
        A=Sudoku()
        A.initialize(T)
        A.BrainSurgery()
        A.insert(T)
        A.linkcut(T)

        T=maxlink(A,T)
#print depth(A.head.right)
