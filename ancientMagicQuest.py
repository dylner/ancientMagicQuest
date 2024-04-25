import pygame
import sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Images/menu.bg.castle.png")
SPLASH_BG = pygame.image.load("Images/splash.loading.png")
SPLASH_ALPHA_INCREMENT = 5  # Adjust the increment for smoother or faster fading

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Font/font.ttf", size)

def splash_screen():
    splash_alpha = 0
    fade_in = True
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((0, 0, 0))  # Fill the screen with black background

        # Update splash screen image with the current alpha value
        splash_with_alpha = SPLASH_BG.copy()
        splash_with_alpha.set_alpha(splash_alpha)
        SCREEN.blit(splash_with_alpha, (0, 0))

        pygame.display.update()

        if fade_in:
            splash_alpha += SPLASH_ALPHA_INCREMENT
            if splash_alpha >= 255:
                splash_alpha = 255
                fade_in = False
        else:
            splash_alpha -= SPLASH_ALPHA_INCREMENT
            if splash_alpha <= 0:
                return  # Exit the function once the splash screen fades out

        clock.tick(30)  # Limit the frame rate to 30 FPS

def play():
    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("PLAY SCREEN", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        import miniGame1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    return  # Return from the play() function

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return  # Return from the options() function

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("ANCIENT MAGIC QUEST", True, "Green")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Images/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Images/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Images/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Load background music and play it
pygame.mixer.music.load("Audio/bg.music.mp3")
pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

splash_screen()  # Display splash screen with fade-in/out effect
main_menu()
