import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from init import Game

FPS = 60

# создаём размеры игрового окна
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# создаём название окна
pygame.display.set_caption('Checkers')
# инициализируем пайгейм и работаем с фоновым аудиофайлом
pygame.init()
pygame.mixer.music.load('image/1st_sound.mp3')
pygame.mixer.music.play(-1)


# получение координат
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# начало игрового процесса
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()