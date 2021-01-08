maze = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
]
N = len(maze)

def is_valid(sol,x,y):
    # print(x,y)
    if x >=0 and x<N and y >=0 and y < N and maze[x][y] == 1:
        return True
    return False

def solver():
    print_maze(maze)
    print("------------")
    sol = [[0 for i in range(N)] for i in range(N)]
    if solver_main(sol,0,0) == True:
        print_maze(sol)
    else:
        print("No solution Available")

def solver_main(sol,x,y):
    # Check if the end of the maze is reached.
    if x == N-1 and y == N-1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if is_valid(sol,x,y):
        sol[x][y] = 1
        if solver_main(sol,x+1,y) == True:
            return True
        if solver_main(sol,x,y+1) == True:
            return True
        sol[x][y] = 0
        return False

def print_maze(x):
    for i in range(N):
        print(x[i])

if __name__ == '__main__':
    solver()
