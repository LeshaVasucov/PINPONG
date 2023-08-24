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
class Player(GameObject):
    def __init__(self, x, y, w, h, image , speed , ):
        super().__init__(x, y, w, h, image , speed)
    def move(self,K_UP,K_DOWN):
        k = pygame.key.get_pressed()
        if k[K_UP]:
            if  self.rect.y >= 0:
                self.rect.y -= self.speed
            
        if k[K_DOWN]:
            if self.rect.y <= 600-self.rect.h :
                self.rect.y += self.speed     
player1 = Player(55,win_h/2 , 25,115,platform_pict ,4 )  
player2 = Player(615,win_h/2 , 25,115,platform_pict ,4 )  
class Ball(GameObject):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image, speed)
    def move():
        pass
ball_pict = pygame.image.load("pinpong_ball.png")
ball = Ball((win_w - 50) / 2   , win_h/2 , 50,50,ball_pict , 2)
while game :
    window.fill(win_fon)
    player1.update()
    player2.update()
    ball.update()
    player1.move(pygame.K_w , pygame.K_s)
    player2.move(pygame.K_UP , pygame.K_DOWN)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    pygame.display.update()
    clock.tick(FPS)