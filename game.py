import pygame
from pygame.locals import *
import random

# Initialize the game
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping pong")

# Set up the colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# Set up the game variables
ball_pos = [screen_width // 2, screen_height // 2]
ball_radius = 10
ball_velocity = [3, 3]

paddle_width, paddle_height = 10, 100
paddle_velocity = 6

paddle1_pos = [0, screen_height // 2 - paddle_height // 2]
paddle2_pos = [screen_width - paddle_width, screen_height // 2 - paddle_height // 2]

# Game loop
running = True
clock = pygame.time.Clock()

misses_player1 = 0
misses_player2 = 0

bounce_count = 0
speed_increment = 0.5
bounces_to_increase_speed = 10

# Menu variables
menu_active = True
menu_font = pygame.font.Font(None, 36)
menu_options = ["Play with computer", "Play with a friend", "Exit"]
selected_option = 0

computer_player1 = False  # Track if computer is playing as player 1

while running:
    while menu_active:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                menu_active = False

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == K_RETURN:
                    if selected_option == 0:
                        # Play with computer
                        computer_player1 = True
                    elif selected_option == 1:
                        # Play with a friend
                        computer_player1 = False
                    elif selected_option == 2:
                        # Exit
                        print("Exiting the game")
                        running = False

                    menu_active = False

        screen.fill(BLACK)
        for i, option in enumerate(menu_options):
            if i == selected_option:
                color = WHITE
            else:
                color = (100, 100, 100)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
            screen.blit(text, text_rect)

        pygame.display.flip()

    if not running:
        break

    # Game logic
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if not computer_player1:  # Control paddle1 if the computer is not player 1
        if keys[K_w] and paddle1_pos[1] > 0:
            paddle1_pos[1] -= paddle_velocity
        if keys[K_s] and paddle1_pos[1] < screen_height - paddle_height:
            paddle1_pos[1] += paddle_velocity

    # Control paddle2 with arrow keys
    if keys[K_UP] and paddle2_pos[1] > 0:
        paddle2_pos[1] -= paddle_velocity
    if keys[K_DOWN] and paddle2_pos[1] < screen_height - paddle_height:
        paddle2_pos[1] += paddle_velocity

    # Computer-controlled paddle1
    if computer_player1:
        # Move paddle1 to follow the ball's y-coordinate
        if paddle1_pos[1] + paddle_height // 2 < ball_pos[1]:
            paddle1_pos[1] += paddle_velocity
        elif paddle1_pos[1] + paddle_height // 2 > ball_pos[1]:
            paddle1_pos[1] -= paddle_velocity

    # Update the ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Handle collisions with the walls
    if ball_pos[1] >= screen_height - ball_radius or ball_pos[1] <= ball_radius:
        ball_velocity[1] = -ball_velocity[1]
        bounce_count += 1

    # Handle collisions with paddles
    if ball_pos[0] <= paddle1_pos[0] + paddle_width and paddle1_pos[1] <= ball_pos[1] <= paddle1_pos[1] + paddle_height:
        ball_velocity[0] = -ball_velocity[0]
        bounce_count += 1
    if ball_pos[0] >= paddle2_pos[0] - ball_radius and paddle2_pos[1] <= ball_pos[1] <= paddle2_pos[1] + paddle_height:
        ball_velocity[0] = -ball_velocity[0]
        bounce_count += 1

    # Handle misses
    if ball_pos[0] < 0:
        misses_player1 += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        if misses_player1 == 5:
            print("Player 2 wins!")
            running = False
    elif ball_pos[0] > screen_width:
        misses_player2 += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        if misses_player2 == 5:
            print("Player 1 wins!")
            running = False

    # Increase ball speed after a certain number of bounces
    if bounce_count >= bounces_to_increase_speed:
        ball_velocity[0] += speed_increment
        ball_velocity[1] += speed_increment
        bounce_count = 0

    # Clear the screen
    screen.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(screen, WHITE, Rect(paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, Rect(paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()

