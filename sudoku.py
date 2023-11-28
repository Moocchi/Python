import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 450, 450
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (50, 50, 50)
SELECTED_CELL_COLOR = (200, 200, 200)

# Font
font = pygame.font.Font(None, 36)

# Sudoku puzzle (0 represents an empty cell)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

selected_cell = None

# Function to draw the Sudoku grid
def draw_grid():
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, GRID_COLOR, (i * (WIDTH // 9), 0), (i * (WIDTH // 9), HEIGHT), thickness)
        pygame.draw.line(screen, GRID_COLOR, (0, i * (HEIGHT // 9)), (WIDTH, i * (HEIGHT // 9)), thickness)

# Function to draw the numbers in the Sudoku grid
def draw_numbers():
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                text = font.render(str(puzzle[i][j]), True, BLACK)
                text_rect = text.get_rect(center=((j * (WIDTH // 9)) + (WIDTH // 18), (i * (HEIGHT // 9)) + (HEIGHT // 18)))
                screen.blit(text, text_rect)

# Function to draw the selected cell
def draw_selected_cell():
    if selected_cell is not None:
        pygame.draw.rect(screen, SELECTED_CELL_COLOR, selected_cell, 3)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // (WIDTH // 9)
            row = y // (HEIGHT // 9)
            selected_cell = pygame.Rect(col * (WIDTH // 9), row * (HEIGHT // 9), WIDTH // 9, HEIGHT // 9)
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit() and selected_cell is not None:
                puzzle[row][col] = int(event.unicode)
                selected_cell = None
            elif event.key == pygame.K_BACKSPACE and selected_cell is not None:
                puzzle[row][col] = 0

    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    draw_selected_cell()

    pygame.display.flip()
