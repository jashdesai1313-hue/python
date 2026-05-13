import pygame
import random
pygame.init()
screen = pygame.display.set_mode((640, 480))
color_sprite1 = (255, 0, 0)
color_sprite2 = (0, 0, 255)
sprite1_rect = pygame.Rect(50, 200, 80, 80)
sprite2_rect = pygame.Rect(300, 200, 80, 80)
sprite1_speed = 3
sprite2_speed = -3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sprite1_rect.x += sprite1_speed
    sprite2_rect.x += sprite2_speed
    if sprite1_rect.right >= 640 or sprite1_rect.left <= 0:
        sprite1_speed = -sprite1_speed
        color_sprite1 = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
    if sprite2_rect.right >= 640 or sprite2_rect.left <= 0:
        sprite2_speed = -sprite2_speed
        color_sprite2 = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color_sprite1, sprite1_rect)
    pygame.draw.rect(screen, color_sprite2, sprite2_rect)
    pygame.display.update()
pygame.quit()