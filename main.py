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

        font = pygame.font.Font(None, 72)
        text_surface = font.render("BUTTON TEST", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(300, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            green_button.handle_event(event)

        green_button.check_hover(pygame.mouse.get_pos())
        green_button.draw(screen)
        pygame.display.flip()


main_menu()