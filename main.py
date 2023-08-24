import pygame
pygame.init()
win_h = 600
win_w = 800
window = pygame.display.set_mode((win_h , win_w))
game = True
FPS = 40
clock = pygame.time.Clock()
while game :
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    pygame.display.update()
    clock.tick(FPS)