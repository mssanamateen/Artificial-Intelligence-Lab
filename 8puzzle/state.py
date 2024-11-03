class State:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
    #this should be changed manually based on n 
    #e.g. it should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0] if n is 4.
    
    greedy_evaluation = None
   
    heuristic = None
    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth

        if parent:
            self.cost = parent.cost + cost

        else:
            self.cost = cost

            
            
    def test(self): #check if the given state is goal
        if self.state == self.goal:
            return True
        return False
        
    


    #heuristic function based on number of misplaced tiles
    def Misplaced_Tiles(self,n): 
        counter = 0;
        self.heuristic = 0
        for i in range(n*n):
            for j in range(n*n):
                if (self.state[i] != self.goal[j]):
                    counter += 1
                self.heuristic = self.heuristic + counter

        self.greedy_evaluation = self.heuristic    
       

        return( self.greedy_evaluation)                
                    


    @staticmethod
    
    #this would remove illegal moves for a given state
    def available_moves(x,n): 
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    #produces children of a given state
    def expand(self , n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]
        
        
            children.append(State(temp, self, direction, self.depth + 1, 1)) #depth should be changed as children are produced
        return children

    
    #gets the given state and returns it's direction + it's parent's direction till there is no parent
    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution
         