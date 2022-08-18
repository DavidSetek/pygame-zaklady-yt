# 4. část - fonty a texty
import pygame

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Systémové fonty
# fonts = pygame.font.get_fonts()
# for one_font in fonts:
#     print(one_font)

# kokila

# Nastavení fontu
system_font = pygame.font.SysFont("kokila", 50)

# Font a text
system_text = system_font.render("Harry Potter", True, white, red)
system_text_rect = system_text.get_rect()
system_text_rect.center = (width//2, height//2)

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Text
    screen.blit(system_text, system_text_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení hry
pygame.quit()
