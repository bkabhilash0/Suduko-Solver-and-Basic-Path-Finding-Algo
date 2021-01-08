import pygame
from solver import valid,find_empty
import copy


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo,i,find):
            bo[row][col] = i
            draw_val(i)

            if solve(bo):
                return True
            bo[row][col] = 0
    return False

pygame.font.init()

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("SUDOKU Solver - BACKTRACKING")
running = True

x = 0
y = 0
dif = 500/9
val = 0

flag1 = 0
flag2 = 0
rs = 0
error = 0

font1 = pygame.font.SysFont("comicsans",40)
font2 = pygame.font.SysFont("comicsans",20)

default =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

grid = copy.deepcopy(default)

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)

# Function to draw required lines for making Sudoku grid
def draw():
    # Draw the lines

    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:

                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153,), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill gird with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    # Draw lines horizontally and verticallyto form grid
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

# Fill value entered in cell
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))

def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT", 1, (0, 0, 0))
    text2 = font2.render("PRESS LCTRL TO SOLVE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))


while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=  False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_LCTRL:
                grid = copy.deepcopy(default)
                solve(grid)
            if event.key == pygame.K_d:
                rs = 0
                flag2 = 0
                print(default)
                grid = copy.deepcopy(default)
    draw()
    draw_box()
    instruction()
    # solve(grid)
    if val != 0:
        draw_val(val)
        grid[int(x)][int(y)]= val
        flag1 = 0
        val = 0
    pygame.display.update()
