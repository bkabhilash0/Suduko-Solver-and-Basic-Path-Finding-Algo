# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]
board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

def print_board(bo):
    for i in range(len(bo)):
        if i%3 == 0 and i != 0:
            print("-------------------------")
        for j in range(len(bo[0])):
            if j % 3 ==0 and j != 0:
                print(" | ",end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ",end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i,j)    # row column
    return None

def valid(bo,num,pos):  # pos = row,column
    # Check in the row and column does the num exists.
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

        box_x = pos[1]//3
        box_y = pos[0]//3

    # Check in the particular Square does the number exists.
    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo,i,find):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False


print_board(board)
print("___________________________________")
solve(board)
print_board(board)
