import pygame
pygame.init()

screen=pygame.display.set_mode((1400,800))
run = True
while run:
    pygame.time.delay(100)
    for event in pygame .event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
