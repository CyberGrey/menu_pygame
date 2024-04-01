import pygame
import sys
from button import ImageButton

pygame.init()
# Параметры экрана
WIDTH, HEIGHT = 1280, 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main menu")
main_background = pygame.image.load("background_img.jpg")               # фоновая картинка



def main_menu():
    # Задаем кнопки главного меню
    start_button = ImageButton(WIDTH/2-(252/2), 500, 252, 74, "НОВАЯ ИГРА", "green_button.jpg", "green_button_hover.jpg", "click.mp3")
    settings_button = ImageButton(WIDTH/2-(252/2), 600, 252, 74, "НАСТРОЙКИ", "green_button.jpg", "green_button_hover.jpg", "click.mp3")
    exit_button = ImageButton(WIDTH/2-(252/2), 700, 252, 74, "ВЫХОД", "green_button.jpg", "green_button_hover.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((220, 220, 220))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("MAIN MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def settings_menu():
    # Задаем кнопки главного меню
    audio_button = ImageButton(WIDTH/2-(252/2), 500, 252, 74, "АУДИО", "green_button.jpg", "green_button_hover.jpg", "click.mp3")
    video_button = ImageButton(WIDTH/2-(252/2), 600, 252, 74, "ВИДЕО", "green_button.jpg", "green_button_hover.jpg", "click.mp3")
    back_button = ImageButton(WIDTH/2-(252/2), 700, 252, 74, "НАЗАД", "green_button.jpg", "green_button_hover.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()

def new_game():

if __name__ == "__main__":
    main_menu()