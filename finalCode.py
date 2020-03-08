# w, h = 3, 3
Matrix = [['?' for x in range(3)] for y in range(3)]
#Lookup = ??
def printBoard( GameBoard):
    for row in range(0,3):
        for col in range(0,3):
            print(Matrix[row][col],end='')
        print()
Matrix = [['?' for x in range(3)] for y in range(3)]
printBoard(Matrix)

def changeCoord(Matrix, rowX, colY,Symbol):
    #change Matrix coordinates at row x col y
    Matrix[rowX] [colY] = Symbol
    #call the function change coord
    changeCoord (Matrix,1,1,'C')
    
#print the board
#printBoard(Matrix)
def main():
    global Matrix
    player1Symbol = 'X'
    player2Symbol= 'O'
    spacesAvailable = 9
    isPlayer1sTurn = True
    isOver = False

    while spacesAvailable > 0 and isOver == False :
        # Step 1: ask user for input
        user_row = input("Enter a row Pos:")
        user_col = input("Enter a col Pos:")
        # Step 2: update the board
        if isPlayer1sTurn == True:
            changeCoord(Matrix, int(user_row), int(user_col), player1Symbol)
        else: 
             changeCoord(Matrix, int(user_row), int(user_col), player2Symbol)
        # Step 3: Print the board
        printBoard(Matrix)
        # Step 4: switch users
        isPlayeris1sTurn = not is Player1sTurn #variable negation
        # Step 5: Check if the Games over
        spacesAvailable = spacesAvailable - 1
        if checkIfPlayerWonGame(Matrix)
    print("Program Finished")
    
    
def printGameBoard(Matrix):
    pass
# Ways to Win
# 1. 3 in a row
# 2. 3 in a column
# 3. 3 diagonally
##Approach 1:  HARD CODE
##Approach 2:  Loop and row / col check
def checkIfPlayerWonGame(GameBoard):
    for i in (3):
        if GameBoard[0][0]== GameBoard[i][1]== GameBoard[i][2]:
            return True
        if GameBoard[i][0] == GameBoard[i][1] == GameBoard[2][i]:
            return True
        if GameBoard[0][2] == GameBoard[1][1] == GameBoard[2][0]:
            return True
        return False
    

if __name__ == "__main__":
    main()
