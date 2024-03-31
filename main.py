import pygame
import sys
from button import ImageButton

pygame.init()
# Параметры экрана
WIDTH, HEIGHT = 600, 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button test")

green_button = ImageButton(WIDTH/2-(252/2), 100, 252, 74, "", "green_button.jpg", "green_button_hover.jpg", "click.mp3")

def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        green_button.draw(screen)
        pygame.display.flip()


main_menu()