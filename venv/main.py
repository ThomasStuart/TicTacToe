player1 = "X"
player2 = "O"
isPlayerOne = True

user_input_col = 0
user_input_row = 0

spacesAvailable = 9
isOver = False

w, h = 3, 3;
Matrix = [['?' for x in range(w)] for y in range(h)]

for row in range(0, 3):
    for col in range(0, 3):
        print(Matrix[row][col], end=" ")
    print()

while spacesAvailable > 0 and isOVer == False:
    # Step 1: ask user for input
    user_input_col = input("Enter a col:  ")
    user_input_row = input("Enter a row:  ")
    # Step 2: update the board
    if isPlayer1 == True:
        Matrix[user_input_col][user_input_row] = player1
    else:
        Matrix[user_input_col][user_input_row] = player2
    # Step 3: Print the board
    # Step 4: Check if someone won
    # Step 5: switch users