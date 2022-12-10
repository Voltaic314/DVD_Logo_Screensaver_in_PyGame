import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the DVD logo image
logo = pygame.image.load("dvd_logo_transparent_white_small.png")

# Set the initial position of the logo
logo_x = random.randint(0, SCREEN_WIDTH - logo.get_width())
logo_y = random.randint(0, SCREEN_HEIGHT - logo.get_height())

# Creating the image_rect
image_rect = logo.get_rect().move(logo_x, logo_y)

# Set the initial velocity of the logo
logo_vx = 3
logo_vy = 3

# Set the background color
bg_color = (0, 0, 0)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update the position of the logo
    logo_x += logo_vx
    logo_y += logo_vy

    # Check if the logo has reached the edge of the screen
    if logo_x < 0 or logo_x > SCREEN_WIDTH - logo.get_width():
        logo_vx = -logo_vx
    if logo_y < 0 or logo_y > SCREEN_HEIGHT - logo.get_height():
        logo_vy = -logo_vy

    # Clear the screen
    screen.fill(bg_color)

    # Draw the logo
    screen.blit(logo, image_rect)
