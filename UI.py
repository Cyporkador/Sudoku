import pygame
import sys
import Solver
import time

pygame.init()
pygame.font.init()
pygame.display.set_caption("Sudoku")

WIDTH = 40*11 + 40
HEIGHT = 40*12 + 40 + 5

BACKGROUND_COLOR = (255, 229, 204)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)

time_sunken = 0

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

correct_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

marked_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)


def new_puzzle():
    global board, correct_board, time_sunken, marked_board
    boards = Solver.generate_new_board()
    board = boards[0]
    correct_board = boards[1]
    marked_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    time_sunken = time.time()


def draw_puzzle_nums():
    my_font = pygame.font.SysFont('comicsans', 45)

    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] != 0:
                text = str(board[i][j])
                label = my_font.render(text, 1, BLACK)
                screen.blit(label, (55 + 44*j, 51 + 44*i))


def draw_marked_nums():
    my_font = pygame.font.SysFont('comicsans', 30)

    for i in range(0, 9):
        for j in range(0, 9):
            if marked_board[i][j] != 0:
                text = str(marked_board[i][j])
                label = my_font.render(text, 1, GREY)
                screen.blit(label, (48 + 44 * j, 48 + 44 * i))


def draw_board():
    for i in range(0, 10):
        pygame.draw.rect(screen, (170, 170, 170), (40, 40 + i*44, 400, 4))
    for i in range(0, 10):
        pygame.draw.rect(screen, (170, 170, 170), (40 + i * 44, 40, 4, 400))
    for i in range(0, 4):
        pygame.draw.rect(screen, BLACK, (40, 40 + i*132, 400, 4))
    for i in range(0, 4):
        pygame.draw.rect(screen, BLACK, (40 + i * 132, 40, 4, 400))


def get_selected_square(pos):
    if 44 < pos[0] < 436 and 44 < pos[1] < 436:
        if pos[0] - 40 >= myround(pos[0] - 40):
            x_coord = myround(pos[0] - 40) + 40
        else:
            x_coord = myround(pos[0] - 40) - 4
        if pos[1] - 40 >= myround(pos[1] - 40):
            y_coord = myround(pos[1] - 40) + 40
        else:
            y_coord = myround(pos[1] - 40) - 4
        if (x_coord, y_coord) == selected_square:
            return -100, -100
        else:
            return x_coord, y_coord
    else:
        return -100, -100


def get_selected_pos(pos):
    return ((pos[0] - 40) // 44), ((pos[1] - 40) // 44)


# helper for drawing red square
def myround(x, base=44):
    return base * round(x/base)


def draw_selected_square(pos):
    pygame.draw.rect(screen, (200, 90, 20), (pos[0], pos[1], 48, 48))
    pygame.draw.rect(screen, BACKGROUND_COLOR, (pos[0] + 4, pos[1] + 4, 40, 40))


def try_to_put_num(pos):
    if marked_board[pos[1]][pos[0]] == 0:
        pass
    elif marked_board[pos[1]][pos[0]] == correct_board[pos[1]][pos[0]]:
        board[pos[1]][pos[0]] = marked_board[pos[1]][pos[0]]
        marked_board[pos[1]][pos[0]] = 0


def draw_new_puzzle_button():
    pygame.draw.rect(screen, (200, 90, 20), (40, 460, 250, 40))
    my_font = pygame.font.SysFont('comicsans', 30)
    text = "Bring on a new puzzle!"
    label = my_font.render(text, 1, BLACK)
    screen.blit(label, (50, 470))


def draw_solved():
    my_font = pygame.font.SysFont('comicsans', 40)
    text = "CONGRATULATIONS!"
    text2 = "PUZZLE COMPLETE!"
    label = my_font.render(text, 1, (255, 100, 0))
    label2 = my_font.render(text2, 1, (255, 100, 0))
    screen.blit(label, (90, 200))
    screen.blit(label2, (100, 240))


def draw_time():
    my_font = pygame.font.SysFont('comicsans', 30)
    total_seconds = (time.time() - time_sunken) // 1
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    if seconds < 10:
        text = "Time: " + str(minutes) + ":" + "0" + str(seconds)
    else:
        text = "Time: " + str(minutes) + ":" + str(seconds)
    label = my_font.render(text, 1, BLACK)
    screen.blit(label, (320, 475))


game_quit = False
selected_square = (-100, -100)
selected_pos = (-4, -4)
new_puzzle()

while not game_quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected_square = get_selected_square(mouse_pos)
            selected_pos = get_selected_pos(selected_square)
            if 350 >= mouse_pos[0] >= 100 and 500 >= mouse_pos[1] >= 460:
                new_puzzle()
        if event.type == pygame.KEYDOWN and selected_pos[0] != -4 and board[selected_pos[1]][selected_pos[0]] == 0:
            if event.key == pygame.K_1:
                marked_board[selected_pos[1]][selected_pos[0]] = 1
            if event.key == pygame.K_2:
                marked_board[selected_pos[1]][selected_pos[0]] = 2
            if event.key == pygame.K_3:
                marked_board[selected_pos[1]][selected_pos[0]] = 3
            if event.key == pygame.K_4:
                marked_board[selected_pos[1]][selected_pos[0]] = 4
            if event.key == pygame.K_5:
                marked_board[selected_pos[1]][selected_pos[0]] = 5
            if event.key == pygame.K_6:
                marked_board[selected_pos[1]][selected_pos[0]] = 6
            if event.key == pygame.K_7:
                marked_board[selected_pos[1]][selected_pos[0]] = 7
            if event.key == pygame.K_8:
                marked_board[selected_pos[1]][selected_pos[0]] = 8
            if event.key == pygame.K_9:
                marked_board[selected_pos[1]][selected_pos[0]] = 9
            if event.key == pygame.K_BACKSPACE:
                marked_board[selected_pos[1]][selected_pos[0]] = 0
            if event.key == pygame.K_RETURN:
                try_to_put_num(selected_pos)

    screen.fill(BACKGROUND_COLOR)
    draw_board()
    draw_selected_square(selected_square)
    draw_puzzle_nums()
    draw_marked_nums()
    draw_new_puzzle_button()
    if board != correct_board:
        draw_time()
    else:
        draw_solved()
    pygame.display.update()
