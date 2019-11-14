
import copy
import time
global result, N
N = 22
result = []



def createBoard(n):
    board = []
    for x in range(n):
        board.append([])
        for y in range(n):
            board[x].append(' ')
    return board



def printBoard(board):
    for x in board:
        print(x)

        

def attacked(board, row, col):
    x = row
    y = col
    
    while (x >= 0):
        if (board[x][y] == 'Q'):
            return True
        x-=1
    
    x = row-1
    y = col-1
    while(x >= 0 and y >= 0):
        if (board[x][y] == 'Q'):
            return True
        x-=1
        y-=1
    
    x = row-1
    y = col+1
    while(x >= 0 and y <= len(board)-1):
        if (board[x][y] == 'Q'):
            return True
        x-=1
        y+=1
        
    return False




def solve(board, row):
    if (row == len(board)):
        result.append(copy.deepcopy(board))
        print("solved")
        if (len(result) == 4):
            return True
        else:
            return False
        
    for col in range(len(board)):
        if (not attacked(board, row, col)):
            board[row][col] = 'Q'
            if (solve(board, row+1) == True):
                return True  
            board[row][col] = ' '
    return False




def nQueens(n):
    board = createBoard(n)   
    if (solve(board, 0)):
        return True
    return False



def print_result(result):
    for sol in result:
        #print()
        #printBoard(sol)
        for x in range(len(sol)):
            for y in range(len(sol)):
                if(sol[x][y] == 'Q'):
                    print("(" + str(x) + "," + str(y) + ") ", end='')
        print()
        print()

##########################################
print("Starting program...\n\n")

start = time.time()

if (not nQueens(N)):
    print("Could not find a solution..")

end = time.time()
print(end-start)
print()
print_result(result)

print("\n\nEnd of program.\n")