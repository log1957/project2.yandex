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

# start screen
def start_screen():
    intro_text = ["АНГЛИЙСКИЕ ШАХМАТЫ", "ЧТОБЫ НАЧАТЬ ИГРУ НАЖМИТЕ ЛЮБУЮ КНОПКУ"
                  ]

    run2 = True
    screen_size = (800, 800)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(pygame.image.load('image/fon.png'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while run2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2 = False
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def end_screen():
    intro_text = ["ИГРА ОКОНЧЕНА"
                  ]

    run2 = True
    screen_size = (800, 800)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(pygame.image.load('image/fon.png'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while run2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2 = False
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


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
    start_screen()

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

    end_screen()


main()