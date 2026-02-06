import pygame
pygame.init()
genislik , yukseklık = 800 , 600
ekran = pygame.display.set_mode((genislik,yukseklık))
player = pygame.Rect(250,250,50,50)
calıstır = True

while calıstır:
    ekran.fill((255,255,255))
    pygame.draw.rect(ekran,(0,0,0),player)
    if pygame.key.get_pressed()[pygame.K_a] == True:
        player.move_ip(-1,0)
    if pygame.key.get_pressed()[pygame.K_d] == True:
        player.move_ip(1,0)
    if pygame.key.get_pressed()[pygame.K_w] == True:
        player.move_ip(0,-1)
    if pygame.key.get_pressed()[pygame.K_s] == True:
        player.move_ip(0,1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calıstır = False
    pygame.display.update()

pygame.quit()