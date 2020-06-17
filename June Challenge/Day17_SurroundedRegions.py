class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l1 = len(board)
        
        if l1 == 0:
            return
        
        l2 = len(board[0])
        
        if l2 == 0 or l2==1:
            return
        
        for i in range(l1):
            if board[i][0]=='O':
                self.color(i,0,board,l1,l2)
            if board[i][l2-1]=='O':
                self.color(i,l2-1,board,l1,l2)
        
        for i in range(l2):
            if board[0][i]=='O':
                self.color(0,i,board,l1,l2)
            if board[l1-1][i]=='O':
                self.color(l1-1,i,board,l1,l2)
        
        for i in range(l1):
            for j in range(l2):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='F':
                    board[i][j] = 'O'
        
    
    def color(self,i,j,board,l1,l2):
        
        if i > l1-1 or i < 0 or j > l2-1 or j < 0:
            return
        
        if board[i][j]=='O':
            board[i][j]='F'
        
        if i > 0 and board[i-1][j]=='O':
            self.color(i-1,j,board,l1,l2)
        
        if j > 0 and board[i][j-1]=='O': 
            self.color(i,j-1,board,l1,l2)
        
        if j < l2-1 and board[i][j+1]=='O': 
            self.color(i,j+1,board,l1,l2)
        
        if i < l1-1 and board[i+1][j]=='O': 
            self.color(i+1,j,board,l1,l2)
        
        return