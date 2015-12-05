class SCCMaker:

    def __init__(self, Matrix):
        self.Matrix = Matrix


    # returns a new matrix with all pointers pointing from j to i
    # instead of i to j
    def flippedGraph(self):
    	toReturn = [[0 for j in self.Matrix[i]] for i in self.Matrix] # Matrix of zeroes

        toReturn = [[0 for j in i] for i in self.Matrix] # Matrix of zeroes
        for i in range(len(self.Matrix)):
            for j in range(len(self.Matrix[i])):
                if self.Matrix[i][j] == 1: 
                    toReturn[j][i] = 1

    	return toReturn
    
    #legal Move from i to j 
    def legalMove(self, i, j): 
    	if self.Matrix[i][j] == 1: 
    		return True

    	return False

   	def getAllLegalMoves(self, i):
   		possibleMoves = []
   		for j in range(len(self.Matrix[i])):

   			if self.legalMove(i, j):
   				possibleMoves.append(j)

   		return possibleMoves

   	def makePostOrder(self):
   		nodesToVisit = set([i for i in range(100)])
   		nodesVisited = set([])
   		postOrder = []

   		def DFS(v):
   			nonlocal nodesVisited
   			nonlocal nodesToVisit
   			nonlocal postOrder

   			nodesToVisit.remove(v)
   			nodesVisited.add(v)

   			for move in getAllLegalMoves(v):
   				if move not in nodesVisited:
   					DFS(move)

   			postOrder = postOrder.insert(0,v)

   		while nodesToVisit:
   			v = nodesToVisit.pop()
   			DFS(v)

   		return postOrder

   	def Kosarajus(self): 
   		postOrder = self.makePostOrder()
   		flipped = SCCMaker(self.flippedGraph())


      ##SHOULD IMPLEMENT DFS FROM FUNCTIONS ALREADY WRITTEN
   		def DFS(v, lst):
   			nonlocal postOrder

   			postOrder.remove(v)
   			for move in flipped.getAllLegalMoves(v):

   				if move in postOrder:
   					lst.append(DFS(move, lst))

   			return lst

=======
        return toReturn

    def legalMove(self, i, j): 
    #legal Move from i to j 
        if self.Matrix[i][j] == 1: 
            return True
        return False

    def getAllLegalMoves(self, i):
        possibleMoves = []
        for j in range(len(self.Matrix[i])):
            if self.legalMove(i, j):
                possibleMoves.append(j)
        return possibleMoves

    def makePostOrder(self):
        nodesToVisit = set([i for i in range(len(self.Matrix))])
        nodesVisited = set([])
        postOrder = []

        def DFS(v):
            nonlocal nodesVisited
            nonlocal nodesToVisit
            nonlocal postOrder
            
            #nodesToVisit.remove(v)
            nodesVisited.add(v)

            for move in self.getAllLegalMoves(v):
                if move not in nodesVisited:
                    DFS(move)
            # This prepends v to postOrder list
            postOrder = [v] + postOrder

        while nodesToVisit:
            v = nodesToVisit.pop()
            DFS(v)

        return postOrder
        
    def Kosarajus(self): 
        postOrder = self.makePostOrder()
        flipped = SCCMaker(self.flippedGraph())
        
        def DFS(v, lst):
            nonlocal postOrder
            
            postOrder.remove(v)
            for move in flipped.getAllLegalMoves(v):
                if move in postOrder:
                    lst.append(DFS(move, lst))
            return lst
            
         return DFS()
        
>>>>>>> refs/remotes/origin/master
