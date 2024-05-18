import pygame
import sys
pygame.init()
size=w,h=(400,400)
posx=80
FPS = 20  # число кадров в секунду
clock = pygame.time.Clock()

sc=pygame.display.set_mode(size)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    if i.type==pygame.MOUSEBUTTONDOWN and i.button==1:
        pygame.draw.circle(sc,(255,255,255),i.pos,20)
        pygame.display.update()
        clock.tick(FPS)
