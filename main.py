import pygame
pygame.init()
win_fon = (15,155,70)
win_h = 600
win_w = 700
window = pygame.display.set_mode((win_w , win_h))
window.fill(win_fon)
game = True
FPS = 40
clock = pygame.time.Clock()
platform_pict = pygame.image.load("platform.png")
class GameObject(pygame.sprite.Sprite):
    def __init__(self , x ,y ,w ,h, image , speed ) :
        super().__init__()
        self.rect = pygame.Rect(x,y,w,h)
        image = pygame.transform.scale(image ,(w,h))
        self.image = image
        self.speed = speed
    def update(self):
        window.blit(self.image, (self.rect.x  ,self.rect.y ))
while game :
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    pygame.display.update()
    clock.tick(FPS)