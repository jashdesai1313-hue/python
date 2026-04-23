import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")
img = pygame.Surface((300, 300))
img.fill((0, 150, 255)) 
if event.type == pygame.QUIT:
    running = False
    screen.fill((58, 58, 58))   
    screen.blit(img, (100, 100)) 
    pygame.display.flip()      
pygame.quit()