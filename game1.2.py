import pygame
import random

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alpha Tauri")

background_color = (135, 206, 235)  # Sky blue
bird_color = (255, 0, 0)  # Red
bullet_color = (0, 0, 0)  # Black

bird_width, bird_height = 50, 30
bird_x = random.randint(0, width - bird_width)
bird_y = random.randint(50, height - bird_height)

bullet_width, bullet_height = 10, 20
bullet_x = width // 2 - bullet_width // 2
bullet_y = height - bullet_height
bullet_speed = 10
bullet_state = "ready"

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    window.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_state = "fired"
                bullet_x = width // 2 - bullet_width // 2
                bullet_y = height - bullet_height

    if bullet_state == "fired":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"
            bullet_y = height - bullet_height

    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    
    if bullet_rect.colliderect(bird_rect):
        score += 1
        bullet_state = "ready"
        bullet_y = height - bullet_height
        bird_x = random.randint(0, width - bird_width)
        bird_y = random.randint50, height - bird_height

    pygame.draw.rect(window, bird_color, bird_rect)
    if bullet_state == "fired":
        pygame.draw.rect(window, bullet_color, bullet_rect)
    
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
